# from django.shortcuts import render
# from django.views.generic.edit import CreateView # type: ignore
# from .forms import SimpleForm
# from .models import SimpleFormEntry


# # Mock data
# cards_data = [
#     {'id': 1, 'card_title': 'Education', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur tortor vel magna tincidunt tempus. Maecenas eget maximus eros. Vivamus id nisl lacus. Donec et risus turpis. In nec efficitur purus, ac faucibus nulla.', 'image': 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmCy16nhIbV3pI1qLYHMJKwbH2458oiC9EmA&s'},
#     {'id': 2, 'card_title': 'Internships', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur tortor vel magna tincidunt tempus. Maecenas eget maximus eros. Vivamus id nisl lacus. Donec et risus turpis. In nec efficitur purus, ac faucibus nulla.', 'image': 'https://images.ctfassets.net/hrltx12pl8hq/28ECAQiPJZ78hxatLTa7Ts/2f695d869736ae3b0de3e56ceaca3958/free-nature-images.jpg?fit=fill&w=1200&h=630'},
#     {'id': 3, 'card_title': 'Projects', 'card_description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla consectetur tortor vel magna tincidunt tempus. Maecenas eget maximus eros. Vivamus id nisl lacus. Donec et risus turpis. In nec efficitur purus, ac faucibus nulla.', 'image': 'https://cdn.pixabay.com/photo/2024/05/26/10/15/bird-8788491_1280.jpg'},
# ]

# def land_page(request):
#     section_name = 'About Me'
#     return render(request, 'imgapp/index.html', {'section_name': section_name, 'cards': cards_data})


# def second_page(request):
#     return render(request, 'includes/cards.html', {'cards': cards_data})


# def detail_page(request, card_id):
#     for c in cards_data:
#         if c['id'] == int(card_id):
#             card = c
#     return render(request, 'imgapp/detail.html', {'card': card})


# class Forms(CreateView):
#       model = SimpleFormEntry
# #     # form_class = MyModelForm  # Optional, if you have a custom form
#       template_name = 'imgapp/simple_form.html'
#       success_url = 'imgapp/form_success.html'  # Redirect to this URL after form submission    
#       fields ="__all__"

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.urls import reverse
from .models import ImgAppDb,Comment
from .forms import post_form
from django.views.generic.edit import CreateView # type: ignore
from django.views.generic import ListView

# class post_page_view(View):
#     def get(self, request):
#         form = post_form()
#         return render(request, 'imgapp/forms.html', {'form': form})

#     def post(self, request):
#         submittedform = post_form(request.POST, request.FILES)

#         if submittedform.is_valid():
#             connect = ImgAppDb(
#                 card_title=submittedform.cleaned_data['card_title'],
#                 card_description=submittedform.cleaned_data['card_description'],
#                 image=submittedform.cleaned_data['Image']  
#             )
#             connect.save()
#             return HttpResponseRedirect(reverse('post_page_view'))  
#         else:
#             print(submittedform.errors)  

#         return render(request, 'imgapp/forms.html', {'form': submittedform})


def land_page(request):
    cards_query = ImgAppDb.objects.all().order_by('-id')[:3]
    section_name = 'About me'
    return render(request, 'imgapp/index.html', {'section_name': section_name, 'cards': cards_query, 'showall': False})

def second_page(request):
    cards_query = ImgAppDb.objects.all()
    return render(request, 'includes/cards.html', {'cards': cards_query, 'showall': True})

def detail_page(request, slug):
    card = ImgAppDb.objects.filter(slug=slug).first()
    return render(request, 'imgapp/detail.html', {'card': card})


def About_us(request):
    return render(request, 'imgapp/AboutUs.html')

def forms_page(request):
    return render(request, 'imgapp/forms.html')

class commentCreateView(CreateView):
    model = Comment
    template_name = "imgapp/comment.html"
    fields = '__all__'
    success_url ='cards'

class post_page_view(CreateView):
    model = ImgAppDb
    template_name = "imgapp/simple_form.html"
    fields = ['card_title', 'image', 'card_description', 'author', 'tags']
    success_url ='Add_Cards'






# base.html

# <!-- {% load static %}
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>{% block page_title %}{% endblock %}</title>
# </head>
# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
# <link rel='stylesheet' href="{% static 'file.css' %}">
# {% block css_files %}
# {% endblock %}

# {% comment %} {% include 'includes/header.html' %}
# {% include 'includes/footer.html' %} {% endcomment %}

# <body>
#     {% block content %}
#     {% endblock %}
   
# </body>
# </html> -->

# <!-- <header class="p-3 bg-dark text-white">
#     <div class="row">
#         <div class="col">
#            <a class="text-decoration-none text-light" href="./index.html"><h3>Raghul's Portfolio</h3></a> 
#         </div>
#         <div class="col">
#             <div class="d-flex justify-content-center gap-3">
#                 <a class="text-light text-decoration-none" href="{% url 'land_page' %}">Home</a>
#                 <a class="text-light text-decoration-none" href="{% url 'second_page' %}">All Cards</a>
#                 <a class="text-light text-decoration-none" href="{% url 'simple_forms' %}">Add Cards</a>
#                 {% comment %} <a class="text-light text-decoration-none" href="">Contact</a> {% endcomment %}
#             </div>
#         </div>
#     </div>
# </header> -->



# <!-- {% extends "base.html" %}
# {% block page_title %} all_cards{% endblock %}

# {% block content %}
# <div class="card-container">
#     {% for card in cards %}
#     <div class="card">
#         <div class="card-title">{{ card.card_title }}</div>
#         <img src="{{ card.image }}" alt="Image {{ card.id }}">
#         <div class="card-description">{{ card.card_description }}</div>
#         <a href="{% url 'detail_page' card_id=card.id %}">More...</a>
#     </div>
#     {% endfor %}    
# </div>
# {% endblock %} -->



