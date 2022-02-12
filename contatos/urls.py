from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('busca', views.busca, name='busca'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
    path('editar_contato/<int:contato_id>', views.editar_contato, name='editar_contato'),
    path('deletar_contato/<int:contato_id>', views.deletar_contato, name='deletar_contato'),
]
