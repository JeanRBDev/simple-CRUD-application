from django.shortcuts import render
from app.forms import UsuarioForm


# Create your views here.
def home(request):
    return render(request, "index.html")


def form(request):
    data = {'form': UsuarioForm()}
    return render(request, "form.html", data)
