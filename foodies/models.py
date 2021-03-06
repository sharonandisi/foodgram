from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tinymce.models import HTMLField
from django.dispatch import receiver


# Create your models here.
class Image(models.Model):
    image_photo = models.ImageField(upload_to = 'photos/')
    caption = models.CharField(max_length =60)
    title = models.CharField(max_length =60)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    # def __str__(self):
    #     return self.profile.id
    class Meta:
        ordering = ['-pub_date']
    @property
    def count_likes(self):
        return self.likes.count()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    def update_caption(self):
        self.update()
   
    @classmethod
    def search_by_title(cls,search_term):
        images = cls.objects.filter(title__icontains=search_term)
        return images   

    class Meta:
        ordering = ["-pk"]
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= "profile")
    first_name = models.CharField(max_length =30)
    surname = models.CharField(max_length =30)
    username = models.CharField(max_length =30)
    avatar = models.ImageField(upload_to = 'avatar', blank=True)
    bio = models.CharField(max_length =30)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()
    def search_profile(self):
        self.search()

class Comments(models.Model):
    comments = models.TextField(blank=True)
    image = models.ForeignKey(Image)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.comments

class Follow(models.Model):
    followers = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'following')

class Likes(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    image = models.ForeignKey(Image)

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name= 'follower')
    following = models.ForeignKey(User, related_name= 'following')
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()