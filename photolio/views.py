from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Location,Cartegory,Images

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')
# Create your views here.
