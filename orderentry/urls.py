from django.urls import path
from . import views
urlpatterns = [
    path('', views.getCustomerInfo, name = 'orderentry'),
]