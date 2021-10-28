from django.urls import path
from . import views
urlpatterns = [
    path('', views.getCustomerInfo, name = 'orderentry'),
    path('', views.getCustomerOrder, name = 'orderentry'),
    path(r'thankyou/', views.thankYou, name = 'thankyou'),
]