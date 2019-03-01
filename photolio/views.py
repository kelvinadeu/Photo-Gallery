from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Location,Cartegory,Images

# Create your views here.
def index(request):
    Images=image.object.all(null=True)
    Location=location.object.all(null=True)
    print(Images)
    return render(request,'index.html',{'images':images,'location':location})
# Create your views here.
