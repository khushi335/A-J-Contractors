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
    path('services/bathroom-renovation/', bathroom_renovation, name='bathroom_renovation'),
    path('services/custom-shelving/',custom_shelving, name='custom_shelving'),
    path('services/steel-welding/', steel_welding, name='steel_welding'),
    path('services/debris-removal/', debris_removal, name='debris_removal'),
]