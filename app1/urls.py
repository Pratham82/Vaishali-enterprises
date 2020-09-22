from django.urls import path
from .import  views
urlpatterns = [
    path('', views.index, name="index"),
    path('contact', views.contact, name="contact"),
    path('services', views.services, name="services"),
    path('work', views.work, name="work"),
    path('<int:id>', views.details_views, name="details")
]