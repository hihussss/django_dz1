from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def home_views(request):
    return HttpResponse("hello")
def get_ingred(request,a):
    temp_recept = 'calculator/index.html'
    servings = int(request.GET.get('servings', 1))
    if servings > 1:
        for i in DATA[a]:
            DATA[a][i] = round(DATA[a][i]*servings,2)

    context = {
        "bludo": a,
        "recipe": DATA[a],
    }
    
    return render(request,temp_recept,context)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
