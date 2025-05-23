from django.shortcuts import render
from django.http import HttpResponse
import random
import string


def home(request):
    return render(request, "generator/home.html", {"password": 'ХуЮмбола'})


def password(request):
    characters = list(string.ascii_lowercase)
    if request.GET.get("uppercase"):
        characters.extend(list(string.ascii_uppercase))

    if request.GET.get("special"):
        characters.extend(list(string.punctuation))

    if request.GET.get("numbers"):
        characters.extend(list(string.digits))

    length = int(request.GET.get("length", 12))
    # Будее взято из запроса request который в свою очередь возьмет это из <select name="length" 12 количество символов по умолчанию>

    thepassword = ''

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, "generator/password.html", {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')