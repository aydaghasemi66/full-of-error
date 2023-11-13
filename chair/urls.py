from django.urls import path
from .views import *


app_name = 'chair'

urlpatterns = [
    path("", ChairListView.as_view(),name='chair'),
    path("chair-detail/<int:pk>",ChairDetailView.as_view(),name="chair_detail"),
    path("payment",PaymentView.as_view(),name="cart"),
]