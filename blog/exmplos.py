import json
import requests

tag_recent = 'https://api.instagram.com/v1/tags/trancoso/media/recent?access_token=6361071795.c966c6f.1e5c3710bf764d3da3ba52bc66b78884'
r = requests.get(tag_recent)
if r.status_code == 200:
    photo = json.loads(r.content)
    photo_url = (photo['data'][0]['images']['standard_resolution']['url'])
else: 
    print ('Erro na conexão, verificar token')

'''        
user_profile = 'https://api.instagram.com/v1/users/6361071795/?access_token=6361071795.c966c6f.1e5c3710bf764d3da3ba52bc66b78884'
r = requests.get(user_profile)
if r.status_code == 200:
    recent_media = json.loads(r.content)
    recent_media = (recent_media['data'][0]['images']['standard_resolution']['url'])

user_recent = 'https://api.instagram.com/v1/users/6361071795/media/recent/?access_token=6361071795.c966c6f.1e5c3710bf764d3da3ba52bc66b78884'
r = requests.get(user_recent)
if r.status_code == 200:
    recent_media = json.loads(r.content)
    profile_picture =  (user['data']['profile_picture'])

, 'recent_media': recent_media, 'profile_picture': profile_picture) '''



{% for photo in photo_url %}
<div>
<img src='{{ photo_url }}' alt='Foto da Hashtag'>
</div>
{% endfor %}
