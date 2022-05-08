from django.test import TestCase
from contatos.models import Categoria, Contato


class ContatoModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        categoria = Categoria.objects.create(nome='TesteCategoria')
        Contato.objects.create(                       
            nome='Nelson', 
            sobrenome='Costa',                               
            categoria=categoria,     
            mostrar=True                                           
            )

    def test_nome_label(self):
        contato = Contato.objects.get(id=1)
        field_label = contato._meta.get_field('nome').verbose_name        
        self.assertEquals(field_label, 'nome')
    
    def test_nome_max_length(self):
        contato = Contato.objects.get(id=1)
        max_length = contato._meta.get_field('nome').max_length
        self.assertEquals(max_length, 20)

    def test_sobrenome_label(self):
        contato = Contato.objects.get(id=1)
        field_label = contato._meta.get_field('sobrenome').verbose_name        
        self.assertEquals(field_label, 'sobrenome')
     
    def test_sobrenome_max_length(self):
        contato = Contato.objects.get(id=1)
        max_length = contato._meta.get_field('sobrenome').max_length
        self.assertEquals(max_length, 20)

    def test_default_mostrar(self):
        contato = Contato.objects.get(id=1)
        default = contato._meta.get_field('mostrar').default
        self.assertEquals(default, True)

    def test_nome_objeto(self):
        contato = Contato.objects.get(id=1)
        nome_objeto = contato.nome
        self.assertEquals(str(contato), nome_objeto)


class CategoriaModelTest(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        categoria = Categoria.objects.create(
            nome='Casa'
        )
    
    def test_nome_label(self):
        categoria = Categoria.objects.get(id=1)
        field_label = categoria._meta.get_field('nome').verbose_name        
        self.assertEquals(field_label, 'nome')
    
    def test_nome_max_length(self):
        categoria = Categoria.objects.get(id=1)
        max_length = categoria._meta.get_field('nome').max_length
        self.assertEquals(max_length, 20)

    def test_nome_objeto(self):
        categoria = Categoria.objects.get(id=1)
        nome_objeto = categoria.nome
        self.assertEquals(str(categoria), nome_objeto)
