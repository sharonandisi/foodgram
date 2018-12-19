from django.db import models
import datetime as dt 
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
class Image(models.Model):
    image_photo = models.ImageField(upload_to = 'photos/')
    caption = models.CharField(max_length =60)
    title = models.CharField(max_length =60)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    def update_caption(self):
        self.update()
    @classmethod
    def present_images(cls):
        present = dt.date.today()
        images = cls.objects.filter(pub_date__date = today)
        return images
    @classmethod
    def days_images(cls,date):
        images = cls.objects.filter(pub_date__date = date)
        return images
    @classmethod
    def search_by_title(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images   
class Profile(models.Models):
    first_name = models.CharField(max_length =30)
    surname = models.CharField(max_length =30)
    username = models.CharField(max_length =30)
    bio = models.CharField(max_length =30)
    email = models.CharField()
    
    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    def search_profile(self):
        self.search()

class Comments(models.Models):
    comments = models.Charfield(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image)
    profile = models.ForeignKey(Profile)
class Likes(models.Models):
    image = models.ForeignKey(Image)

class Follow(models.Model):
    followers = models.ForeignKey(Profile)
    following = models.ForeignKey(Profile)

