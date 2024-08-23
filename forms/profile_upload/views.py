from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import Profileform
from .models import ProfileImage1
from django.views.generic.edit import CreateView # type: ignore
from django.views.generic import ListView
# def store_file(file):
#     with open('temp/userimage.jpg','+wb') as dest:
#         for chunk in file.chunks():
#             dest.write(chunk)
 
# class CreateProfileView(View):
#     def get(self, request):
#         form = Profileform()
 
#         return render(request,'profileupload/profile_index.html',{
#             'form':form
#         })
 
#     def post(self, request):
#         submittedform = Profileform(request.POST,request.FILES)
 
#         if submittedform.is_valid():
#             store_file(request.FILES['userimage'])
#             # userimage=request.FILES.get('userimage')
#             # Name=request.POST.get('Name')
#             # profile = ProfileImage1(userimage=userimage, Name=Name)
#             # profile.save()
#             return HttpResponseRedirect('/profile')
#         return render(request,'profileupload/profile_index.html',{
#             'form':submittedform
#         })
    
class CreateProfileView(CreateView):
    model = ProfileImage1
    template_name = "profile_upload/user_upload.html"
    success_url ='/profile/'
    fields ="__all__"
    
class Profileview(ListView):
      model = ProfileImage1
      template_name = "profile_upload/rendering_image.html"
      context_object_name = 'renderingimg'
      