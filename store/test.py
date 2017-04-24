from django.test import TestCase
from .models import Book, Author
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from decimal import *


class StoreViewsTestCase(TestCase):
    def setUp(self):
        ##hay que crear los datos ya que los test se hacen sobre una copia vacia del a bbdd principal
        self.user = User.objects.create_user(username="james", email="some@email.com", password="password")
        author = Author.objects.create(first_name="Stephen", last_name="King")
        book = Book.objects.create(title="Cujo", author=author, description="Darn scary!", price=9.99, stock=1)

    def test_index(self):
        resp = self.client.get('/store/')
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('books' in resp.context)
        self.assertTrue(resp.context['books'].count() > 0)

    def test_cart(self):
        resp = self.client.get('/store/cart/')
        self.assertEqual(resp.status_code, 302)
        ##302 por que no esta logado

    def test_book_detail(self):
        resp = self.client.get('/store/book/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.context['book'].pk, 1)        ##comprueba que la cable es la misma que consulta
        self.assertEqual(resp.context['book'].title, "Cujo")
        resp = self.client.get('/store/book/2/')
        self.assertEqual(resp.status_code, 404)             #no existe el libro 2

    def test_add_to_cart(self):
        self.logged_in = self.client.login(username="james", password="password")
        self.assertTrue(self.logged_in)
        resp = self.client.get('/store/add/1/')
        resp = self.client.get('/store/cart/')
        self.assertEqual(resp.context['total'], Decimal('9.99'))
        self.assertEqual(resp.context['count'], 1)
        self.assertEqual(resp.context['cart'].count(), 1)
        self.assertEqual(resp.context['cart'].get().quantity, 1)
