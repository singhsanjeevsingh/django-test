from unicodedata import name
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    # path('', views.register,name="register"),
    path("",views.login,name="login"),
    path("register",views.register,name="register"),
    path("home",views.home,name="home")
]
