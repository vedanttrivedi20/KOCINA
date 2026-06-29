from django.shortcuts import render
import requests
import random


BASE_URL = "https://www.themealdb.com/api/json/v1/1/"


# ----------------------------
# Helper Function
# ----------------------------

def get_vegetarian_meals(keyword=""):

    meals = []

    if keyword:

        url = BASE_URL + f"search.php?s={keyword}"

        response = requests.get(url)

        data = response.json()

        if data["meals"]:

            for meal in data["meals"]:

                if meal["strCategory"] == "Vegetarian":

                    ingredients = []

                    for i in range(1, 21):

                        ingredient = meal.get(f"strIngredient{i}")
                        measure = meal.get(f"strMeasure{i}")

                        if ingredient and ingredient.strip():

                            ingredients.append({
                                "ingredient": ingredient,
                                "measure": measure
                            })

                    meals.append({
                        "id": meal["idMeal"],
                        "name": meal["strMeal"],
                        "image": meal["strMealThumb"],
                        "category": meal["strCategory"],
                        "area": meal["strArea"],
                        "instructions": meal["strInstructions"],
                        "youtube": meal["strYoutube"],
                        "ingredients": ingredients
                    })

    return meals


# ----------------------------
# HOME
# ----------------------------

def home(request):

    search = request.GET.get("recipe", "").strip()

    meals = []

    no_results = False

    if search:

        meals = get_vegetarian_meals(search)

        if not meals:
            no_results = True

    featured = get_vegetarian_meals("Vegetarian")

    trending = get_vegetarian_meals("Pasta")

    context = {

        "search_query": search,

        "meals": meals,

        "featured": featured[:3],

        "trending": trending[:3],

        "no_results": no_results

    }

    return render(request, "recipes/home.html", context)


# ----------------------------
# CATEGORY
# ----------------------------

def category(request, keyword):

    meals = get_vegetarian_meals(keyword)

    return render(request, "recipes/home.html", {

        "meals": meals,

        "search_query": keyword,

        "featured": [],

        "trending": [],

        "no_results": len(meals) == 0

    })


# ----------------------------
# RANDOM RECIPE
# ----------------------------

def random_recipe(request):

    url = BASE_URL + "filter.php?c=Vegetarian"

    response = requests.get(url)

    data = response.json()

    meal = random.choice(data["meals"])

    recipe = get_vegetarian_meals(meal["strMeal"])

    return render(request, "recipes/home.html", {

        "meals": recipe,

        "featured": [],

        "trending": [],

        "search_query": "",

        "no_results": False

    })


# ----------------------------
# ABOUT
# ----------------------------

def about(request):

    return render(request, "recipes/about.html")


# ----------------------------
# CONTACT
# ----------------------------

def contact(request):

    return render(request, "recipes/contact.html")