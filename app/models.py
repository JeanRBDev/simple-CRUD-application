from django.db import models
from project_crud import settings


# Create your models here.


class Usuario(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11, unique=True)
    ano_nascimento = models.IntegerField()
