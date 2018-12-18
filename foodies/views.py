from django.shortcuts import render, redirect
from .models import Image
# Create your views here.
def index(request):
    date = dt.date.today()
    images = Image.present_images()
    return render(request, 'index.html', {"date": date, "images":images})

def profile(request):
    return render(request, 'all-photos/profile.html')

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-photos/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})