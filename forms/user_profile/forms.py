from django import forms
from .models import Review
class forms_page_class(forms.Form):
    user_name = forms.CharField(
        label='Enter Your Name : ',
        max_length=6,
        min_length=3,
        error_messages={
            'required': 'Please enter your name',
            'min_length': 'Please enter at least 3 characters',
        }
    )
    text = forms.CharField(label='Enter the Feedback',widget=forms.Textarea,error_messages={'required': 'Please enter at Feedback'})
    rating = forms.IntegerField(label='Enter the Rating',min_value=1,max_value=5,error_messages={'required': 'Please enter Rating'})

class forms_page11(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__' #['user_name',rating]
        #exclude = []
        labels = {
            'user_name':'Your Name'
        }