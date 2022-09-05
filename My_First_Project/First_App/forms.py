from django import forms
from django.core import validators
#from First_App.models import Album, Musicians
from First_App import models

class MusicianForm(forms.ModelForm):
    class Meta:
        model = models.Musicians
        fields ='__all__'

class AlbumForm(forms.ModelForm):
    release_date= forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model = models.Album
        fields ='__all__'

