from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import Review
from django.views.generic import TemplateView
from django.views.generic import ListView
from .forms import forms_page11  # Import the correct form

class FormspageView(View):
    def get(self, request):
        form = forms_page11()  # Use the ModelForm here
        return render(request, 'user_profile/forms.html', {'form': form})

    def post(self, request):
        form = forms_page11(request.POST)  # Use the ModelForm here
        if form.is_valid():
            form.save()  # Now this will work because forms_page11 is a ModelForm
            return HttpResponseRedirect('/user/Thanks/')
        return render(request, "user_profile/forms.html", {"form": form})

class ThankYouView(TemplateView):
    template_name = "user_profile/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Messgae"] = "Hi I'm Here"
        return context


class formlistView(ListView):
    model = Review
    context_object_name = "reviews"
    template_name = "user_profile/userlist.html"
    print(context_object_name)


# def forms_page(request):
#     if request.method == 'POST':
#         form = forms_page_class(request.POST)
#         if form.is_valid():
#             review = Review(
#                 user_name=form.cleaned_data['user_name'],
#                 text=form.cleaned_data['text'],
#                 rating=form.cleaned_data['rating'],
#             )
#             review.save()
#             return HttpResponseRedirect('/user/Thanks')
#         else:
#             return render(request, 'user_profile/forms.html', {'form': form})
#     else:
#         form = forms_page_class()
#         return render(request, 'user_profile/forms.html', {'form': form})

# def Thanks(request):
#     return render(request, 'user_profile/thank_you.html')