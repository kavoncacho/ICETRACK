from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path(r'aboutus/', views.aboutus, name = 'aboutus'),
]