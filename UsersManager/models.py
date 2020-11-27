from django.db import models
from uuid import uuid4
from abc import ABC,ABCMeta, abstractmethod
# Create your models here.


class Usuario(models.Model):
    user_id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=40)

    def __init__(self, name, username, password):
        self.user_id = self.generateId()
        self.name = name
        self.username = username
        self.password = password

    def generateId(self):
        return 1

    def __str__(self):
        return f"{self.name} ({self.username})"

    @abstractmethod
    def getRole(self):
        pass


class Gerencia(Usuario):

    def getRole(self):
        return "g"


class Taller(Usuario):

    def getRole(self):
        return "t"


class Ventas(Usuario):

    def getRole(self):
        return "v"


class ProfesionalMedico(Usuario):

    def getRole(self):
        return "p"


class Secretaria(Usuario):

    def getRole(self):
        return "s"
