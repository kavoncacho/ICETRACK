from django.urls import path
from . import views
urlpatterns = [
    path('', views.customer_Information, name = 'orderentry'),
]