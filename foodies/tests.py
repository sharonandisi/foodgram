from django.test import TestCase
from .models import Image,Profile,Comments,Likes
import datetime as dt

# Create your tests here.
class ProfileTestClass(TestCase):
    #set up method
    def setUp(self):
        self.sharon = Profile(first_name = 'Sharon', last_name= 'Andisi', username = 'migidza_andisi', bio = 'pray,love,laugh', email = 'sharonandisi.sa@gmail.com')
    
    #testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.sharon,Profile))

        # Testing Save Method
    def test_save_method(self):
        self.sharon.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.sharon= Editor(first_name = 'sharon', last_name ='andisi', username = 'migidza_andisi', bio = 'pray,love,laugh', email ='sharonandisi.sa@gmail.com')
        self.sharon.save_editor()


    def tearDown(self):
        Profile.objects.all().delete()
        Image.objects.all().delete()

    def present_images(self):
        test_date = '2018-12-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        images_by_date = Article.days_news(date)
        self.assertTrue(len(images_by_date) == 0)