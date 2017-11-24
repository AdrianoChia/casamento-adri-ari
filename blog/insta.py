import json
import requests
import dropbox
import urllib

tag_recent = 'https://api.instagram.com/v1/tags/becodobatman/media/recent?access_token=6361071795.c966c6f.1e5c3710bf764d3da3ba52bc66b78884'
r = requests.get(tag_recent)
photo = json.loads(r.content)
foto = photo['data'][0]['images']['standard_resolution']['url']
urllib.request.urlretrieve(foto, 'img/teste.jpg')
access_token = 'UQ0p70bOHWAAAAAAAAAADUwHjPwgPCOsI7p6-yMDF0g-LV4C4_lTiuRgfSdkvazw'
file_from = 'img/teste.jpg'
file_to = '/Fotos/teste.jpg'
dbx = dropbox.Dropbox(access_token)
f = open(file_from, 'rb')
dbx.files_upload(f.read(), file_to)