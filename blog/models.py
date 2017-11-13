from django.db import models
from django.utils import timezone


class RSVP(models.Model):
    convidado = models.CharField(max_length=200)
    acompanhante = models.IntegerField(default=0)
    comentario = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    
    def publish(self):
        self.created_date = timezone.now()
        self.save

    def __str__(self):
        return (self.convidado)

class oauth(models.Model):
    user_ID = models.TextField(default='c966c6fc09974becaa208180e8f5aa44')
    client_secret = models.TextField(default='93375efa5f3f4055a9740bfc6367121d')
    grant_type = models.TextField(default='authorization_code')
    redirect_uri = models.TextField(default='adrianochia.pythonanywhere.com/tag')
    code = models.TextField(default='14421ece8c3642aca864a3a01f37980f')
