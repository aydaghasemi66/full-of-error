from django.shortcuts import render , redirect
# from accounts.models import CustomeUser
from django.contrib import messages
from django.views.generic import TemplateView, RedirectView

# # Create your views here.






class HomeView(TemplateView):
    template_name = 'root/index.html'



def about (request):
    if request.method == 'GET' :
        return render(request,"root/about.html",)
    

# def contact(request):
#     if request.method =='GET':

#         return render(request,"root/contact.html")

    



