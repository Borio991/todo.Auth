from django.urls import path, include
from . import views

urlpatterns = [


    # Home
    path('', views.home, name="home"),

    # AUTH
    path('signup/', views.signupuser, name="signupuser"),
    path('logout/', views.logoutuser, name="logoutuser"),
    path('login/', views.loginuser, name="loginuser"),

    # Todo
    path('current/', views.currenttodo, name="currenttodo"),

]
