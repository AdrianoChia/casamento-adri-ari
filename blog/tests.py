from django.test import TestCase

import json
import requests
import dropbox
import urllib

# Create your tests here.
def tag(request):
	tag = 'becodobatman'
	user_id = '2945569'
	api_instagram = 'https://api.instagram.com/v1'
	access_token_instagram = '6361071795.c966c6f.1e5c3710bf764d3da3ba52bc66b78884'
	tag_recent = api_instagram + '/tags/' + tag + '/media/recent?access_token=' + access_token_instagram
	user_recent = api_instagram + '/users/' + user_id + '/media/recent/?access_token=' + access_token_instagram
	r = requests.get(tag_recent)
#	r = requests.get(user_recent)
	if r.status_code == 200:
		photo = json.loads(r.content)
		m = 0
		a = [photo['data'][0]['carousel_media'][m]]
		if not a:
			foto = photo['data'][0]['images']['standard_resolution']['url']
		else:
			while (m <= 100):
					foto = photo['data'][0]['carousel_media'][m]['images']['standard_resolution']['url']
					m = m + 1
	else:
		print ('Erro na conexão, verificar token')
	return render(request, 'blog/tag.html', {'foto': foto})

urllib.request.urlretrieve(foto, 'img/teste.jpg')

access_token_dbx = 'UQ0p70bOHWAAAAAAAAAADUwHjPwgPCOsI7p6-yMDF0g-LV4C4_lTiuRgfSdkvazw'
file_from = 'img/teste.jpg'  #local file path
file_to = '/Fotos/teste.jpg'  # dropbox path

def upload_file(file_from, file_to):
    dbx = dropbox.Dropbox(access_token_dbx)
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)
	upload_file(file_from,file_to)