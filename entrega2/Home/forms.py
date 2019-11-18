from django import forms

from .models import Recup, Coment


class Recup(forms.ModelForm):

    class Meta:
        model = Recup
        fields = ('user', 'passs',)

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ('coment', 'descri')