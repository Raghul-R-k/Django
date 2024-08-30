# from django import forms

# class SimpleForm(forms.Form):
#     # Define your form fields here
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     message = forms.CharField(max_length=500)
from django import forms
from .models import ImgAppDb

class post_form(forms.Form):
    card_title = forms.CharField(max_length=100)
    card_description = forms.CharField(widget=forms.Textarea)
    Image = forms.FileField()
class PostForm(forms.ModelForm):
    class Meta:
        model = ImgAppDb
        fields = ['card_title', 'image', 'card_description', 'author', 'tags']
