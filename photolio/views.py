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

def search_cartegory(request):

    if 'cartegory' in request.GET and request.GET["cartegory"]:
        search_term = request.GET.get("cartegory")
        searched_images = Images.search_cartegory(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"images": searched_images,"location":location})

    else:
        message = "You haven't searched for any cartegory"
        return render(request, 'search.html',{"message":message,"location":location})
