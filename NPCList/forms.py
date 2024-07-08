from django import forms
from .models import NPC

class NPCentries(forms.ModelForm):
    class Meta:
        model = NPC
        fields = ('name', 'genre')
