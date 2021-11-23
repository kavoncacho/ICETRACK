from django.urls import path
from . import views
urlpatterns = [
    path(r'continue/', views.getCustomerInfo, name = 'continueorder'),
    path('', views.getCustomerOrder, name = 'orderentry'),
    path(r'thankyou/', views.thankYou, name = 'thankyou'),
]