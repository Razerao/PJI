from django.db import models
from usuarios.models import Usuario
from datetime import datetime

class Avisos(models.Model):
    nome = models.CharField(max_length = 50)
    data = models.DateField()
    descricao = models.TextField()
    avisos = models.FileField(upload_to = "avisos")
    class Meta:
        verbose_name = 'Aviso'
        verbose_name_plural = 'Avisos'
    def __str__(self) -> str:
        return self.nome


class Atas(models.Model):
    nome = models.CharField(max_length = 50)
    data = models.DateField()
    descricao = models.TextField()
    atas = models.FileField(upload_to = "atas")
    class Meta:
        verbose_name = 'Ata'
        verbose_name_plural = 'Atas'
    def __str__(self) -> str:
        return self.nome



class Outros(models.Model):
    nome = models.CharField(max_length = 50)
    data = models.DateField()
    descricao = models.TextField()
    outros = models.FileField(upload_to = "outros")
    class Meta:
        verbose_name = 'Outro'
        verbose_name_plural = 'Outros'
    def __str__(self) -> str:
        return self.nome

class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)
    comentario = models.TextField()
    data = models.DateTimeField(default = datetime.now)
    
    
    def __str__(self) -> str:
        return self.usuario.nome