from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'apartamento', 'email', 'senha')
    search_fields = ('nome', 'email', 'apartamento')
    readonly_fields = ('senha',)
