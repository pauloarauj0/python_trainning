from django.urls import path
from .views import index, register_restaurant, user_login, user_register, user_logout
from django.contrib import admin

urlpatterns = [
    path('', index, name='index'),
    path('user_login/', user_login, name='user_login'),
    path('register/', user_register, name='register'),
    path('user_logout/', user_logout, name='user_logout'),

    #path('reserve/', reserve, name='reserve'),
    path('register_restaurant', register_restaurant, name='register_restaurant'),
]