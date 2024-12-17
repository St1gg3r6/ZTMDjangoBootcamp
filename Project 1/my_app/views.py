from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def about(request):
    return HttpResponse("My name is Steve.")


def hello(request, first_name):
    return HttpResponse(f'Hello {first_name}')


def add(request, num_one, num_two):
    return HttpResponse(f'The sum of your nummbers is {num_one + num_two}')
