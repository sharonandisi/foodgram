from django import forms
from .models import Image, Profile, Comments

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')
    
class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'pub_date']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ImageUpload(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date', 'profile']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['pub_date', 'image', 'profile']
        fields = ['comments']
        widgets = {
            'comments':forms.TextInput(attrs={
                'class': u'comments-input form-control', 'placeholder': u'Insert Comment'})
        }

class profileEdit(forms.Form):
    name = forms.CharField(max_length=20)
    username = forms.CharField(max_length=20)
    Bio = forms.Textarea()
    Email = forms.EmailField()
    phone_number = forms.CharField(max_length=12)
    