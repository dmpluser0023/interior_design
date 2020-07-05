from django.shortcuts import render,redirect
from .forms import Quate_form

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = Quate_form(request.POST)
        form.save()
        return redirect('index')
    else:
        form = Quate_form()
    return render(request,'index.html',{'form':form})

def about(request):
    if request.method == 'POST':
        form = Quate_form(request.POST)
        form.save()
        return redirect('index')
    else:
        form = Quate_form()
    return render(request,'about.html',{'form':form})

def services(request):
    if request.method == 'POST':
        form = Quate_form(request.POST)
        form.save()
        return redirect('index')
    else:
        form = Quate_form()
    return render(request,'services.html',{'form':form})

def projects(request):
    if request.method == 'POST':
        form = Quate_form(request.POST)
        form.save()
        return redirect('index')
    else:
        form = Quate_form()
    return render(request,'projects.html',{'form':form})

def contact(request):
    if request.method == 'POST':
        form = Quate_form(request.POST)
        form.save()
        return redirect('index')
    else:
        form = Quate_form()
    return render(request,'contact.html',{'form':form})