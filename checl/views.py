from django.shortcuts import render, redirect
from .models import Candidate
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Read
@login_required(login_url='login')
def home(request):
    candidate=Candidate.objects.all()
    return render(request, 'home.html', {"candidates":candidate})

# Create

def add(request):
    if request.method=="POST":
        if request.POST.get('name') and \
            request.POST.get('ville') and \
            request.POST.get('assertion1') and \
            request.POST.get('assertion2') and \
            request.POST.get('assertion3') and \
            request.POST.get('assertion4') and \
            request.POST.get('assertion5') and \
            request.POST.get('assertion6') and \
            request.POST.get('assertion7') and \
            request.POST.get('assertion8') and \
            request.POST.get('assertion9') and \
            request.POST.get('gender'):
           
            candidate = Candidate()
            candidate.name=request.POST.get('name')
            candidate.ville=request.POST.get('ville')
            candidate.gender=request.POST.get('gender')
            candidate.assertion1=request.POST.get('assertion1')
            candidate.assertion2=request.POST.get('assertion2')
            candidate.assertion3=request.POST.get('assertion3')
            candidate.assertion4=request.POST.get('assertion4')
            candidate.assertion5=request.POST.get('assertion5')
            candidate.assertion6=request.POST.get('assertion6')
            candidate.assertion7=request.POST.get('assertion7')
            candidate.assertion8=request.POST.get('assertion8')
            candidate.assertion9=request.POST.get('assertion9')
            candidate.save()
            return HttpResponseRedirect('succes')
    else:
            return render(request, 'add.html')


def succes(request):
    return render(request, "succes.html")

def logn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Bienvenue  ' + str(user)) 
            return redirect('home')
        else:
            messages.error(request, "erreur d'autentification")
    return render(request, 'login.html', {'message':messages})


def edit(request, id):
    candidate=Candidate.objects.get(id=id)
    return render(request, 'edit.html', {"Candidate":candidate})