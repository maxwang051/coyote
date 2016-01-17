from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
    temp_ing = ingredients.split('+')
    search_string = ''
    for ingredient in temp_ing:
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
        'ingredients': ingredients,
    }

    return render(request, 'recipes_list.html', context)

def detail_view(request, recipe_id, ingredients):
    ingredients = ingredients.split('+') # list of ingredients owned

    response = unirest.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/" + recipe_id + "/information",
      headers={
        "X-Mashape-Key": "QN5CLcAiQXmshOrib4vl7QifQAPjp1MjXoijsnsKdgztp93FnI"
      }
    )

    needed = []

    for ingredient in response.body["extendedIngredients"]:
        needed.append(ingredient["name"])

    missing = list(set(needed) - set(ingredients))

    print missing

    recipe = unirest.get("https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/extract?forceExtraction=false&url=http%3A%2F%2F" + response.body['sourceUrl'][7:].replace("/", "%2F") + "",
      headers={
        "X-Mashape-Key": "QN5CLcAiQXmshOrib4vl7QifQAPjp1MjXoijsnsKdgztp93FnI"
      }
    )
    context = {
        'recipe': response.body,
        'directions': recipe.body
    }

    return render(request, 'recipe_detail.html', context)

@csrf_exempt
def sms(request):
    twiml = '<Response><Message>Hello there!!!!!!!</Message></Response>'
    return HttpResponse(twiml, content_type='text/xml')
