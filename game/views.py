from django.shortcuts import render
from random import choice

# lista_slow = []
#
# with open("slowa.txt", 'r', encoding="utf-8") as file:
#     print("Inicjalizuje liste slow!")
#     for el in file.readlines():
#         lista_slow.append(el.strip())
#
# lista_slow = set(lista_slow)
# print("Przekonwertowano na set")


def lobby(request):
    template = 'lobby.html'
    context = {

    }
    return render(request, template, context)


def game(request):
    template = 'game.html'
    # rand = choice(tuple(lista_slow))
    context = {
        # "slowo": rand
    }
    return render(request, template, context)
