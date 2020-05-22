from django.shortcuts import render
from random import choice

lista_slow = []

with open("slowa.txt", 'r', encoding="utf-8") as file:
    print("Inicjalizuje liste slow!")
    for el in file.readlines():
        lista_slow.append(el.strip())

lista_slow = set(lista_slow)
print("Przekonwertowano na set")


def index(request):
    template = 'index.html'
    rand = choice(tuple(lista_slow))
    context = {
        "slowo": rand
    }
    return render(request, template, context)
