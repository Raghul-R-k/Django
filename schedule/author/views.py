
# Create your views here.
from django.shortcuts import render # type: ignore
from django.http import Http404 # type: ignore
from .models import author
from django.db.models import Avg # type: ignore

def author_list(request):
    authors = author.objects.all().order_by('first_name')
    auth_count = authors.count() #select count(*) from authors
    auth_rating = authors.aggregate(Avg('rating')) 
    return render(request, 'author/index.html', {
        'authors': authors,
        'author_count': auth_count,
        'author_rating': auth_rating['rating__avg'],
    })

def author_detail(request, author_id):
        authors = author.objects.get(id=author_id)
        return render(request, 'author/author_detail.html', {'author': authors})

# def author_detail(request,slug):
#       authors = author.objects.get(slug=slug)
#       return render(request,'author/author_detail.html',{'author':authors})

