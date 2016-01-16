from django.shortcuts import redirect, render
from django.http import HttpResponse
from recipes.forms import IngredientForm
import unirest

def home_page(request):

    return HttpResponse('<h1>Home Page</h1>')

def choose_ingredients(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            picked = form.cleaned_data.get('picked')
            ingredients = ''
            for ing in picked:
                ingredients += ing + '+'
    else:
        form = IngredientForm
        return render(request, 'choose_ingredients.html', {'form' : form})

    return redirect('/recipes/list/%s' % ingredients)

def recipe_list(request, ingredients):
    ingredients = ingredients.split('+')
    search_string = ''
    for ingredient in ingredients:
        search_string += ingredient + "%2C"

    search_string = search_string[:-6]
    print(search_string)

    response = unirest.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients?ingredients=" + search_string + "&number=10",
      headers={
        "X-Mashape-Key": "QN5CLcAiQXmshOrib4vl7QifQAPjp1MjXoijsnsKdgztp93FnI",
        "Accept": "application/json"
      }
    )

    context = {
        'recipes': response,
    }

    return render(request, 'recipes_list.html', context)

def detail_view(request, recipe_id):
    response = unirest.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/+" + recipe_id + "/information",
      headers={
        "X-Mashape-Key": "QN5CLcAiQXmshOrib4vl7QifQAPjp1MjXoijsnsKdgztp93FnI"
      }
    )

    context = {
        'recipe': response.body
    }

    return render(request, 'recipe_detail.html', context)
