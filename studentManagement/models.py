from django.db import models


# Create your models here.
class Student(models.Model):
    """
    Classe responsável pelo cadastro de alunos
    """
    name = models.CharField(max_length=50, blank=False)
    matricula = models.CharField(max_length=20, blank=False, default="0")
    idade= models.CharField(max_length=2, blank=False, default='0')
    email= models.EmailField(max_length=254, blank=False, default='example@email.com')
    telefone= models.CharField(max_length=14, blank=False, default='+55 12 345678900')
    
