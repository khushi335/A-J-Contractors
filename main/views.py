from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")

def service(request):
    return render(request,"main/service.html")

def project(request):
    return render(request,"main/project.html")

def contact(request):
    return render(request,"main/contact.html")
    
def interior_demolition(request):
    return render(request, 'main/interior_demolition.html')

def exterior_demolition(request):
    return render(request, 'main/exterior_demolition.html')
    
def kitchen_renovation(request):
    return render(request, 'main/kitchen_renovation.html')
    
def bathroom_renovation(request):
    return render(request, 'main/bathroom_renovation.html')
    
def custom_shelving(request):
    return render(request, 'main/custom_shelving.html')