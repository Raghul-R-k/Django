from django.shortcuts import render # type: ignore
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect # type: ignore

# Create your views here.
def Webpage1(request):
    
        page = 'This is first WebPage'
        return HttpResponse(page)
    
def Webpage2(request):
    
        page = 'This is second WebPage'
        return HttpResponse(page)
  
def Webpage3(request):
 
        page = 'This is third WebPage'
        return HttpResponse(page)
    