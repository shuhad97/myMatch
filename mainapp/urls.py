 
 
 
from django.contrib import admin
from django.urls import path
from . import views

 
 
urlpatterns = [
    path('', views.index),
    path('login/', views.loginPage, name='login' ),
    path('signup/', views.signupPage, name ='signup'),
    path('loginProcess/', views.loginProcess, name = 'loginProcess'),
    path('signup/signupProcess', views.signupProcess, name='signupProcess'),
    path('signup/courses', views.courses, name = 'coursesList'),
    path('profile/', views.profile, name= 'profile'),
    path('mymatches/', views.mymatches, name = 'mymatches'),
    path('mymatches/getmatches/', views.getMatches, name = 'getmatches'),

 ]