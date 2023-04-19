from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    return render(request, 'besk/index.html')
def contact(request):
    contact = Contact.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('post')
        if not phone:
            phone = None
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(name=name, phone=phone, email=email, message=message)
        contact.save()
        return redirect('index')
    return render(request, 'besk/contact.html')
def about(request):
    teams = Team.objects.all()
    context={
        'teams' : teams
    }
    return render(request, 'besk/about.html', context)
def projeimage(request):
    images = ProjectImage.objects.all()
    context={
        'images' : images
    }
    return render(request, 'besk/projeimage.html', context)
def acad(request):
    program = Program.objects.filter(name = "ACAD")
    context = {
        'program' : program
    }
    return render(request, 'besk/program.html', context)

def dsmax(request):
    program = Program.objects.filter(name = "3DSMAX")
    context = {
        'program' : program
    }
    return render(request, 'besk/program.html', context)

def probina(request):
    program = Program.objects.filter(name = "PROBINA")
    context = {
        'program' : program
    }
    return render(request, 'besk/program.html', context)

def sta4cad(request):
    program = Program.objects.filter(name = "STA4CAD")
    context = {
        'program' : program
    }
    return render(request, 'besk/program.html', context)

def referans(request):
    referanslar = Proje.objects.all()
    context = {
        'referanslar' : referanslar
    }
    return render(request, 'besk/referans.html', context)
def faaliyet(request):
    fa1 = Faaliyet.objects.get(id = 1)
    fa2 = Faaliyet.objects.get(id = 2)
    fa3 = Faaliyet.objects.get(id = 3)
    fa4 = Faaliyet.objects.get(id = 4)
    fa5 = Faaliyet.objects.get(id = 5)
    fa6 = Faaliyet.objects.get(id = 6)
    fa7 = Faaliyet.objects.get(id = 7)
    faaliyet1 = FaaliyetKonu.objects.filter(faaliyet_id = 1)
    faaliyet2 = FaaliyetKonu.objects.filter(faaliyet_id = 2)
    faaliyet3 = FaaliyetKonu.objects.filter(faaliyet_id = 3)
    faaliyet4 = FaaliyetKonu.objects.filter(faaliyet_id = 4)
    faaliyet5 = FaaliyetKonu.objects.filter(faaliyet_id = 5)
    faaliyet6 = FaaliyetKonu.objects.filter(faaliyet_id = 6)
    faaliyet7 = FaaliyetKonu.objects.filter(faaliyet_id = 7)
    context = {
        'faaliyet1' : faaliyet1,
        'faaliyet2' : faaliyet2,
        'faaliyet3' : faaliyet3,
        'faaliyet4' : faaliyet4,
        'faaliyet5' : faaliyet5,
        'faaliyet6' : faaliyet6,
        'faaliyet7' : faaliyet7,
        'fa1' : fa1,
        'fa2' : fa2,
        'fa3' : fa3,
        'fa4' : fa4,
        'fa5' : fa5,
        'fa6' : fa6,
        'fa7' : fa7,
    }
    return render(request, 'besk/faaliyet.html', context)