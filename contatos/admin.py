from django.contrib import admin
from .models import Categoria, Contato


# Informações que estarão disponíveis na área do ADMIN.
class ContatoAdmin(admin.ModelAdmin):  
    list_display = ('id', 'nome', 'sobrenome', 'telefone',
                    'email', 'data_criacao', 'categoria', 'mostrar')
    list_display_links = ('nome', 'id', 'sobrenome')
    list_per_page = 10
    list_editable = ('mostrar', 'telefone')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
