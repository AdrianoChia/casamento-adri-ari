from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def contato(request):
    return render(request, 'blog/contato.html')
def home(request):
    return render(request, 'blog/home.html')
def galeria(request):
    return render(request, 'blog/galeria.html')
def rsvp(request):
    return render(request, 'blog/rsvp.html')
def evento(request):
    return render(request, 'blog/evento.html')
def lista_presentes(request):
    return render(request, 'blog/lista_presentes.html')



# Create your views here.
