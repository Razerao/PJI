from django.contrib import admin
from .models import Avisos, Atas, Outros, Comentarios

admin.site.register(Avisos)
admin.site.register(Atas)
admin.site.register(Outros)
admin.site.register(Comentarios)