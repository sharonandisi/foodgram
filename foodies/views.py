from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Image, Comments
import datetime as dt
from django.db import transaction
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import NewsLetterForm, ProfileForm, profileEdit, ImageUpload, CommentForm
from django.contrib.auth.decorators import login_required

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
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            article.save()
        return redirect('index')

    else:
        form = ImageUpload()
    return render(request, 'new_image.html', {"form":form})


def profile(request, user_id):
    images = Image.objects.all()
    return render(request, 'profile.html', {"images":images})

@login_required(login_url='/accounts/login/')
def profile_edit(request, user_id):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile', user_id)
        else:
            messages.error(request, ('Error'))
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit-profile.html', {"profile_form": profile_form})


@login_required(login_url='/accounts/login/')
def comment(request, id):
    current_user = request.user
    image = Image.objects.get(pk=id)
    comment = Comments.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.writer = current_user
            comment.image = image
            comment.save()
            return redirect('index')
    else:
        form = CommentForm()
    
    return render(request, "comment.html", {"form":form, "image":image, "comment":comment})