from django import forms
class Profileform(forms.Form):
    userimage = forms.FileField()
    Name = forms.CharField( max_length=50,required=False)