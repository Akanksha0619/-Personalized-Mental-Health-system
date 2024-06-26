from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


from django.urls import path
from . import views




urlpatterns = [

    path('home/', views.home, name="home"),
    path('register/', views.register_user, name="register"),
    path('', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('contact_form/', views.contact_form, name="contact_form"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('search-history/', views.search_history_view, name='search_history'),
    path('profile_view/', views.profile_view, name='profile'),
    path('search/', views.search_view, name='search'),




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
         name='password_reset_complete')
 ]


