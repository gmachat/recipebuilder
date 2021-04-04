from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'recipes'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('get_ingredients/', views.get_ingredients, name='get_ingredients'),
    path('get_ingredient/<int:food_id>/', views.get_ingredient, name='get_ingredient'),
    path('search_ingredients/', views.search_ingredients, name="search_ingredients"),

    path('get_recipe/<int:recipe_id>', views.get_recipe, name="get_recipe"),
    path('create_recipe/', views.create_recipe, name="create_recipe"),

]
