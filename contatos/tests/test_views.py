from django.test import TestCase, Client
from django.urls import reverse
from contatos.models import Contato, Categoria

class IndexViewTest(TestCase):

    def setUp(self):
        self.cliente = Client()
        self.url = reverse('index')        
        categoria = Categoria.objects.create(nome='TesteCategoria')

        contatos = 7

        for contato in range(contatos):
            Contato.objects.create(
                nome=f'Christian {contato}',
                sobrenome=f'Surname {contato}',
                categoria=categoria,
            )            
        return super().setUp()

    def test_view_ok(self):
        response = self.cliente.get(self.url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'contatos/index.html')

    def test_pagination_is_five(self):
        response = self.client.get(self.url)        
        self.assertEquals(response.status_code, 200)
        self.assertTrue('contatos' in response.context)                
        self.assertEqual(len(response.context['contatos']), 5)
    
    def test_pagination_next_page(self):
        response = self.client.get(reverse('index')+'?p=2')        
        self.assertEqual(response.status_code, 200)
        self.assertTrue('contatos' in response.context)        
        self.assertEqual(len(response.context['contatos']), 2)

