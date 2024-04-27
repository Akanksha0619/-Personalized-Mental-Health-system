from django.urls import path
from .views import *
urlpatterns = [
  
  path('home/', home, name="home"),
  path('register/',register_user,name="register"),
  path('', login_user, name="login"),
  path('logout/',logout_user,name="logout"),

  
]