from django.db import models

# Create your models here.
class Image(models.Model):
    image_photo = models.ImageField(upload_to = 'photos/')
    caption = models.CharField(max_length =60)
    title = models.CharField(max_length =60)
    profile = models.ForeignKey(Profile)
    pub_date = models.DateTimeField(auto_now_add=True)



class Profile(models.Models):
    first_name = models.CharField(max_length =30)
    surname = models.CharField(max_length =30)
    username = models.CharField(max_length =30)
    bio = models.CharField(max_length =30)
    email = models.CharField()
    
    
class Comments(models.Models):
    comments = models.Charfield(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image)
class Likes(models.Models):
    image = models.ForeignKey(Image)

