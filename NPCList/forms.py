from django import forms
from .models import NPC
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class NPCentries(forms.ModelForm):
    class Meta:
        model = NPC
        fields = ('name', 'genre', 'job', 'description')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.template_pack = 'bootstrap5'
        self.helper.label_class = 'col-form-label'
        self.helper.field_class = 'form-control'
        self.helper.add_input(Submit('submit', 'Create NPC'))





