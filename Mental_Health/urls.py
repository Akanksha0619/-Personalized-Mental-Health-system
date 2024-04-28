from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

# urls.py
from django.urls import path
<<<<<<< HEAD
from .views import profile_view



urlpatterns = [
    path('home/', views.home, name="home"),
    path('register/', views.register_user, name="register"),
    path('', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),

    path('profile_view/', profile_view, name='profile'),



    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'
         ),
         name='password_reset_complete'),]



=======
from .views import *
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
  
  path('home/', home, name="home"),
  path('register/',register_user,name="register"),
  path('', login_user, name="login"),
  path('logout/',logout_user,name="logout"),
  path('password_reset/', auth_views.PasswordResetView. as_view(), name='password_reset'),
  path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
  path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
  path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
<<<<<<< HEAD
  path('profile_view/', profile_view, name='profile_view'),
  path('contact/', contact_form, name='contact_form'),
  path('edit_profile/', edit_profile, name='edit_profile'),
  
  
]
=======
  path('profile/', profile_view, name='profile'),
]
>>>>>>> 350f9ad34db95c79f8eae526011254450f6b977c
>>>>>>> 967c7b562581d0740427a4c0ebeb0e57d51fd579
