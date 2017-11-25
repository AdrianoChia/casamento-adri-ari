import json
import requests
import dropbox
import urllib

def hashtag(request):
    tag = 'becodobatman'
    api_instagram = 'https://api.instagram.com/v1'
    access_token_instagram = '6361071795.c966c6f.1e5c3710bf764d3da3ba52bc66b78884'
    tag_recent = api_instagram + '/tags/' + tag + '/media/recent?access_token=' + access_token_instagram
    r = requests.get(tag_recent)
    grupo_foto = []
    if r.status_code == 200:
        photo = json.loads(r.content)
        for dados in photo['data']:
            foto = dados['images']['standard_resolution']['url']
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
    else:
        print ('Erro na conexão, verificar token')  
    return render(request, 'blog/tag.html', {'grupo_foto': grupo_foto})
