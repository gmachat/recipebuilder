from django.forms import ModelForm
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'cook_time', 'prep_time', 'ingredients']


