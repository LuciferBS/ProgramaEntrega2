from django import forms

from .models import Recup

class Recup(forms.ModelForm):

    class Meta:
        model = Recup
        fields = ('user', 'passs',)