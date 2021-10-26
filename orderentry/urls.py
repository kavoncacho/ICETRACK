from django.urls import path
from . import views
urlpatterns = [
    path('', views.OrderEntryView.as_view(), name = 'orderentry'),
]