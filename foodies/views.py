from django.shortcuts import render, redirect
from .models import Image
from .forms import NewsLetterForm
from django.contrib.auth.decorators import login_required.
# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    date = dt.date.today()
    images = Image.present_images()
    

    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name =name,email =email)
            recipient.save()
            send_welcome_email(name,email)

            HttpResponseRedirect('index')
    else:
        form = NewsLetterForm()
    
    return render(request, 'index.html', {"date": date, "images":images, "letterForm":form})
@login_required(login_url='/accounts/login/')
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

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            article.save()
        return redirect('index')

    else:
        form = NewImageForm()
    return render(request, 'new_image.html', {"form":form})
