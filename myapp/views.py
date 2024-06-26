from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def main(request):
    return render(request, 'main.html')


def orel_rechka(request):
    return HttpResponse(choice(['орел','решка']))


def kosty(request):
    return HttpResponse(randint(1, 6))


def sto(request):
    return HttpResponse(randint(1, 100))
