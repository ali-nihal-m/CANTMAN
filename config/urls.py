from os import name
from zipfile import Path

from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.registeration, name='registeration'),
    path('register_post/' , views.register_post, name='register_post'),

    path('login/', views.user_login, name='login'),
    path('login_post/' , views.login_post, name='login_post'),

    path('home/' , views.home, name='home'),

    path('add_food/' , views.add_food, name='add_food'),
    path('add_food_post/' , views.add_food_post, name='add_food_post'),

    path('food_list/' , views.food_list, name='food_list'),

    path('edit_food/<int:id>/' , views.edit_food, name='edit_food'),
    path('edit_food_post/<int:id>/' , views.edit_food_post, name='edit_food_post'),

    path('delete_food/<int:id>/' , views.delete_food, name='delete_food'),

    path('logout/', views.user_logout, name='logout'),
    path('delete_user/' , views.delete_user, name='delete_user'),
]
