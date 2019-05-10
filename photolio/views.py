from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Location,Cartegory,Images

# Create your views here.
def index(request):
    images=Images.objects.all()
    location=Location.objects.all()
    print(Images)
    return render(request,'index.html',{'images':images,'location':location})
# Create your views here.



def sport(request):
    # sports=Images.objects.filter_by()
    return render(request,'sports.html',)

def search_cartegory(request):

    if 'cartegory' in request.GET and request.GET["cartegory"]:
        search_term = request.GET.get("cartegory")
        searched_images = Cartegory.objects.filter(name=search_term)
        images = [images.id for images in searched_images]
        # print(images)
        image = Images.objects.filter(id__in=images)


        return render(request, 'search.html',locals())

    else:
        message = "You haven't searched for any cartegory"
        return render(request, 'search.html',{"message":message,"location":location})
