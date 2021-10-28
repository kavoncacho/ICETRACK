from django.urls import path
from . import views
urlpatterns = [
    path('', views.getTicketInfo, name = 'ticketmanage'),
    path(r'ticketsent/', views.sorry, name = 'sorry'),
]