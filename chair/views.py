from typing import Any
from django.db import models
from django.shortcuts import render , get_object_or_404, redirect
from .models import Chair
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, TemplateView
from .cart import Cart




class ChairListView(ListView):
    
    template_name = 'chair/shop.html'
    context_object_name = 'chair'
    paginate_by = 2

    def get_queryset(self):
        return Chair.objects.filter(status=True) 
    def post(self, request, *args, **kwargs):
        post_detail = ChairDetailView()
        return post_detail.post(request,*args,**kwargs)

    
class ChairDetailView(DetailView):
     model = Chair
     template_name = 'chair/cart.html'
     context_object_name = 'chair'

    
     def post(self, request, *args, **kwargs):
         cart = Cart(request)
        
         if 'id' in request.POST :
             product = get_object_or_404(Chair, id=int(request.POST['id']))    
             cart.delete_from_cart(product)
            
         else:
             product = get_object_or_404(Chair, id=int(request.POST['pk']))
             quantity = int(request.POST['quantity'])
             cart.add_to_cart_some_quantity(product, quantity)
            
         return redirect(request.path_info)

    
class PaymentView(TemplateView):
     template_name = 'chair/cart.html'

     def post(self, request, *args, **kwargs):
         cart = Cart(request)
         cart.clear()
         return redirect(request.path_info)


    