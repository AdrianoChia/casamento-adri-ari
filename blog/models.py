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

class grupo_foto(models.Model):
    grupo_foto = models.TextField()
'''
class tag(models.Model):
    tag = models.CharField(max_length=20)
    def __str__(self):
        return (self.tag)'''