from django import forms

from .models import RSVP, oauth

class RSVPForm(forms.ModelForm):

    class Meta:
        model = RSVP
        fields = ('convidado', 'acompanhante', 'comentario')

class oauthForm(forms.ModelForm):

    class Meta:
        model = oauth
        fields = ('user_ID', 'client_secret', 'grant_type', 'redirect_uri', 'code')
