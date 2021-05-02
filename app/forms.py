from django.forms import ModelForm, TextInput, CharField
from app.models import Usuario


# Create the form class.
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'cpf', 'ano_nascimento']
        widgets = {
            'first_name': TextInput(attrs={'placeholder': 'test'}),
            'last_name': TextInput(attrs={'placeholder': 'test'}),
            'cpf': TextInput(attrs={'placeholder': 'test',
                                    'data-mask': '000 000 000 00'}),
            'ano_nascimento': TextInput(attrs={'placeholder': 'test'}),
        }