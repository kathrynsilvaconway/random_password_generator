from django.shortcuts import render, redirect
import random
import string
from random import choice

def index(request):
    request.session.flush()
    return render(request, 'index.html')

def generate_password(request):
    password = ""
    length = request.POST['length']
    length = int(length)
    letters = string.ascii_letters +string.digits +'!'+'&'+'?'+'#'+'$'+'%'+'*'
    for x in range(length):
        password += random.choice(letters)
    request.session['password'] = password
    request.session['length'] = length
    return redirect('/render_password')

def regenerate_password(request, length):
    password = ""
    letters = string.ascii_letters +string.digits +'!'+'&'+'?'+'#'+'$'+'%'+'*'
    for x in range(length):
        password += random.choice(letters)
    request.session['password'] = password
    request.session['length'] = length
    return redirect('/render_password')
    

def render_password(request):
    context = {
        'password': request.session['password'],
        'length': request.session['length']
    }
    return render(request, 'render_password.html', context)

# Create your views here.