from django.shortcuts import render, HttpResponse, redirect

from django.http import JsonResponse

# Create your views here.

def index(request, my_val):
    return HttpResponse(f"this is the same as @app.route({my_val}")

def fromthesix(request):
    return HttpResponse('Veiws from the 6ix')


def redirected_method(request):
    return JsonResponse({"response": "JSON response from redirected_method", "status": True})