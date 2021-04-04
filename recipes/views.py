from django.shortcuts import render, redirect
from .models import Recipe, UserProfile
from .forms import RecipeForm
import requests
import json, pprint

API_KEY='8xedfIcHQ3TEztrl1gwLiUpHm84Aww3f876PaMnt'

def query_ingredients(food_id):
    return requests.get(f'https://api.nal.usda.gov/fdc/v1/food/{food_id}?api_key={API_KEY}').json()

def home(request):
    return render(request, 'recipes/home.html')

def get_ingredients(request):
    response = requests.get(f'https://api.nal.usda.gov/fdc/v1/foods/list?api_key={API_KEY}')
    data = response.json()
    print(data)
    return render(request, 'recipes/ingredients_list.html', {'data': data})

def get_ingredient(request, food_id):
    return render(request, 'recipes/ingredient_info.html', {'data': query_ingredients(food_id)})

def search_ingredients(request,):
    search_query = request.GET.get('search_input')
    response = requests.get(f'https://api.nal.usda.gov/fdc/v1/foods/search?api_key={API_KEY}&query={search_query}')
    data = response.json()
    return render(request, 'recipes/search_ingredients.html', {'data': data, 'search': search_query})

def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        # can only handle 1 input at the moment
        print(form)
        if form.is_valid():
            user_profile = UserProfile.objects.get(id = request.user.id)
            recipe = form.save(commit=False)
            jsonIngredients = json.dumps({"ingredients": str(recipe.ingredients).split('') })
            recipe.ingredients = jsonIngredients
            recipe.created_by = user_profile
            recipe.save()
            print(user_profile.created_recipes)
            # user_profile.recipes_created
            # print(user_profile.recipes_created)
        return redirect('recipes:get_recipe', recipe_id=recipe.id)
        # return redirect('recipes:get_recipe', id=recipe.id)
    else:
        form = RecipeForm()
        return render(request, 'recipes/recipe_form.html', {'form':form})



# if request.method == 'POST':
#         form = GroupForm(request.POST)
#         if form.is_valid():
#             user = User.objects.get(id=request.user.id)
#             group = form.save(commit=False)
#             group.owner = user
#             group.save()
#             group.users.add(user)
#             user_profile = UserProfile.objects.get(user=user)
#             user_profile.groups.add(group)
#             return redirect('meetup:group_detail', group_id=group.id)

def get_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    user_creator = recipe.created_by.user.username
    ingredient_list = json.loads(recipe.ingredients)['ingredients']
    ingredients = []
    nutrients = {}
    
    url = f'https://api.nal.usda.gov/fdc/v1/foods?api_key={API_KEY}'

    payload = {
  "fdcIds": ingredient_list,
  "format": "abridged",
  "nutrients": [
    203,
    204,
    205
  ]
    }

    try:
        res = requests.post(url, json=payload).json()
    except:
        print('something went wrong')

    for ingredient in res:
        ingredients.append(ingredient)
        for nutrient in ingredient['foodNutrients']:
            if nutrient['name'] in nutrients:
                nutrients[nutrient['name']] += nutrient['amount'] 
            else:
                nutrients[nutrient['name']] = nutrient['amount'] 
    print(recipe.created_by)
    
    return render(request, 'recipes/recipe_page.html', {'recipe': recipe, 'ingredients': ingredients, 'nutrients': nutrients, 'res': res, 'created_by': user_creator})
