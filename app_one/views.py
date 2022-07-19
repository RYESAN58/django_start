from ast import Return
from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("this is the same as @app.route('/")
