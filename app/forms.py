from django.forms import ModelForm
from app.models import Usuario


# Create the form class.
class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'cpf', 'ano_nascimento']