from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import RSVP, foto
from .forms import RSVPForm
from django.contrib.auth.decorators import login_required
import json
import requests

def contato(request):
    return render(request, 'blog/contato.html')

def home(request):
    return render(request, 'blog/home.html')

def galeria(request):
    return render(request, 'blog/galeria.html')

def rsvp(request):
	if request.method == "POST":
		form = RSVPForm(request.POST)
		post = form.save(commit = 'false')
		post.created_date = timezone.now()
		post.save()
		return redirect('blog/rsvp.html')
	else:
		form = RSVPForm()
	return render(request, 'blog/rsvp.html', {'form': form})

def evento(request):
    return render(request, 'blog/evento.html')

def lista_presentes(request):
    return render(request, 'blog/lista_presentes.html')

def lista_convidados(request):
	lista = RSVP.objects.all().order_by('convidado')
	return render(request, 'blog/lista_convidados.html', {'lista': lista})

def tag(request):
	tag_recent = 'https://api.instagram.com/v1/tags/becodobatman/media/recent?access_token=6361071795.c966c6f.1e5c3710bf764d3da3ba52bc66b78884'
	r = requests.get(tag_recent)
	if r.status_code == 200:
		photo = json.loads(r.content)
		foto = {photo['data'][0]['carousel_media'][0]['images']['standard_resolution']['url'], photo['data'][0]['carousel_media'][1]['images']['standard_resolution']['url'], photo['data'][0]['carousel_media'][2]['images']['standard_resolution']['url']}
	else:
		print ('Erro na conexão, verificar token')
	return render(request, 'blog/tag.html', {'foto': foto})



# Create your views here.
