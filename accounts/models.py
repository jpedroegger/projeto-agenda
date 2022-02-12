from contatos.models import Contato
from django import forms


# Model do formulário.
class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('data_criacao',)

