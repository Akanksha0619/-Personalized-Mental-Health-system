
from django.urls import path
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
  path('profile/', profile_view, name='profile'),
]