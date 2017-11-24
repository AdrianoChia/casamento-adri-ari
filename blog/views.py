from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import RSVP, grupo_foto
from .forms import RSVPForm
from django.contrib.auth.decorators import login_required
import json
import requests
import dropbox
import urllib

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
'''
def tag(request):
	if request.method == "POST":
		form = tagForm(request.POST)
		post = form.save()
		return redirect('')
		#user_id = '2945569'
	else:
		post = 'becodobatman'
	return render(request, 'blog/tag.html', {'post': post})
'''
def hashtag(request):
	tag = 'becodobatman'
	api_instagram = 'https://api.instagram.com/v1'
	access_token_instagram = '6361071795.c966c6f.1e5c3710bf764d3da3ba52bc66b78884'
	tag_recent = api_instagram + '/tags/' + tag + '/media/recent?access_token=' + access_token_instagram
	r = requests.get(tag_recent)
	grupo_foto = []
	if r.status_code == 200:
		photo = json.loads(r.content)
		m = 0
		while (m < 100):
			if (photo['data'][m]['images']['standard_resolution']['url']):
				foto = photo['data'][m]['images']['standard_resolution']['url']
				nome_foto = foto.replace('/', '')
				urllib.request.urlretrieve(foto, 'img/' + nome_foto)
				access_token_dbx = 'UQ0p70bOHWAAAAAAAAAADUwHjPwgPCOsI7p6-yMDF0g-LV4C4_lTiuRgfSdkvazw'
				file_from = 'img/' + nome_foto
				file_to = '/Fotos/' + nome_foto
				dbx = dropbox.Dropbox(access_token_dbx)
				f = open(file_from, 'rb')
				dbx.files_upload(f.read(), file_to)
				f.close()
				grupo_foto = grupo_foto + [foto]
				m += 1
			else:
				m = 100		
	else:
		print ('Erro na conexão, verificar token')	
	return render(request, 'blog/tag.html', {'grupo_foto': grupo_foto})





# Create your views here.
