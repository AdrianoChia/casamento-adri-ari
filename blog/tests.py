from django.test import TestCase

import json
import requests
import dropbox

# Create your tests here.
def tag(request):
	tag_recent = 'https://api.instagram.com/v1/tags/becodobatman/media/recent?access_token=6361071795.c966c6f.1e5c3710bf764d3da3ba52bc66b78884'
	r = requests.get(tag_recent)
	if r.status_code == 200:
		photo = json.loads(r.content)
		n = 0
		m = 0
		a = [photo['data'][n]['carousel_media'][m]]
		foto = {}
		while (n <= 100):
			if not a:
				while (n <= 100):
					foto = {photo['data'][n]['images']['standard_resolution']['url']}
					n = n + 1
			else:
				while (m <= 100):
						foto = photo['data'][n]['carousel_media'][m]['images']['standard_resolution']['url']
						m = m + 1
			n = n + 1
	else:
		print ('Erro na conexão, verificar token')
	return ({'foto": foto'})	
#	return render(request, 'blog/tag.html', {'foto': foto})


def dropbox(request):
	dbx  = dropbox.Dropbox('UQ0p70bOHWAAAAAAAAAADUwHjPwgPCOsI7p6-yMDF0g-LV4C4_lTiuRgfSdkvazw')
	dbx.users_get_current_account()

import dropbox

access_token = 'UQ0p70bOHWAAAAAAAAAADUwHjPwgPCOsI7p6-yMDF0g-LV4C4_lTiuRgfSdkvazw'
file_from = 'img/teste.jpg'  //local file path
file_to = '/Fotos/teste.jpg'  // dropbox path

def upload_file(file_from, file_to):
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)
upload_file(file_from,file_to)