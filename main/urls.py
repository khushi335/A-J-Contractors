from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name="index"),
    path("about/",about,name="about"),
    path("service/",service,name="service"),
    path("project/",project,name="project"),
    path("contact/",contact,name="contact"),
    path('services/interior-demolition/', interior_demolition, name='interior_demolition'),
    path('services/exterior-demolition/', exterior_demolition, name='exterior_demolition'),
    path('services/kitchen-renovation/', kitchen_renovation, name='kitchen_renovation'),
    path('services/bathroom-renovation/', views.bathroom_renovation, name='bathroom_renovation'),
]