from django.test import TestCase
from .models import Image,Profile,Comments,Likes


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