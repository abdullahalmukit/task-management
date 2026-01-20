from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Wellcome to the task management system")

def contact(request):
    return HttpResponse("<h3 style='color: red'>Email: abdullahalmukit287@gmail.com</h3><h4 style='color:green'>Phone: +8801796124352</h4>")

def show_task(request):
    return HttpResponse("This is our task page")

def show_specific_task(request, id):
    print("id" ,id)
    print("id type", type)
    return HttpResponse(f"This is show task management {id}")

def dashboard(request, id):
    return HttpResponse("This is my dashboard")