from django.shortcuts import render, redirect
from app.forms import UsuarioForm
from app.models import Usuario


# Create your views here.
def home(request):
    data = {'db': Usuario.objects.all()}
    return render(request, "index.html", data)


def form(request):
    data = {'form': UsuarioForm()}
    return render(request, "form.html", data)


def create(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
