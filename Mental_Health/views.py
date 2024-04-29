from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import  CreateUserForm,ProfileForm
from .models import *
from django.http import HttpResponseRedirect 
from django.urls import reverse

@login_required
def profile_view(request):
    # Retrieve the profile associated with the authenticated user
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        # If profile does not exist, create a new one
        profile = Profile.objects.create(user=request.user, email=request.user.email)

    # Pass the profile instance to the template context
    return render(request, 'profile_view.html', {'profile': profile})

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('login')



def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        # Perform form validation
        if not name or not email or not message:
            messages.error(request, 'Please fill out all fields.')
        else:
            # Save the contact message to the database
            Contact.objects.create(
                name=name,
                email=email,
                message=message
            )

            # Redirect to the home page with success parameter
            return redirect('home')

    return render(request, 'contact_form.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_view')  # Redirect to profile page after saving
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})


@login_required
def display_history(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')  # assuming you're getting search query from a form
        search_result = perform_search(search_query)  # your search function, this is just a placeholder
        SearchHistory.objects.create(user=request.user, search_statement=search_query, search_result=search_result)
        # perform other operations with search results
    return render(request, 'display_history.html')







import pickle
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
import re
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')








@login_required
def search_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')




        # Process search query using machine learning model and pipeline
        search_results = process_query(search_query)

        # Save search history
        SearchHistory.objects.create(user=request.user, search_statement=search_query, search_result=search_results)

        # Render search results
        return render(request, 'search_results.html', {'search_query': search_query, 'search_results': search_results})
    else:
        # Render the search form
        return render(request, 'search.html')
with open('clean_text.pkl', 'rb') as read_file:
    clean_text = pickle.load(read_file)
with open('df.pkl', 'rb') as read_file:
    df = pickle.load(read_file)
with open('get_top_k_predictions.pkl', 'rb') as read_file:
    s = pickle.load(read_file)
X = df['Problem']
y = df['combined']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipeline = make_pipeline(TfidfVectorizer(), RandomForestClassifier(random_state=42))
pipeline.fit(X_train, y_train)

from nltk.corpus import stopwords
STOPWORDS = set(stopwords.words('english'))
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\W+', ' ', text)  # Remove all non-word characters
    text = ' '.join(word for word in text.split() if word not in STOPWORDS)  # Remove stopwords
    return text

def get_top_k_predictions(model, vectorizer, text, k):
    tfidf_matrix = vectorizer.transform([text])
    probabilities = model.predict_proba(tfidf_matrix)
    top_k_indices = np.argsort(-probabilities[0])[:k]
    print("Probabilities shape:", probabilities.shape)
    print("Top k indices:", top_k_indices)
    return [(model.classes_[i], probabilities[0][i]) for i in top_k_indices]



def process_query(search_query):
    # Clean text
    user_problem = clean_text(search_query)

    # Get top k predictions
    top_5 = get_top_k_predictions(pipeline.named_steps['randomforestclassifier'],pipeline.named_steps['tfidfvectorizer'], user_problem, k=5)
    predicted_results = []
    for pred in top_5:
        if '|' in pred[0]:
            symptom, solution = pred[0].split('|', 1)  # Split at the first occurrence of '|'
            predicted_results.append((symptom, solution))
        else:
            predicted_results.append((pred[0], None))

    return predicted_results


# Placeholder for other views...
def home(request):
    return render(request, 'home.html')

def register_user(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('home')  # Redirect to the home page after successful registration
    else:
        form = CreateUserForm()
    return render(request, 'register_page.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'Welcome back, {username}! You are now logged in.')
            return redirect('home')  # Adjust the URL name to your home page
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('login')

    return render(request, 'login_page.html')
from django.shortcuts import render
from .models import SearchHistory

def search_history_view(request):
    search_history = SearchHistory.objects.all()
    return render(request, 'search_history.html', {'search_history': search_history})
