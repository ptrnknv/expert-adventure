from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from products.models import Product


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store')
        self.assertTemplateUsed(response, 'products/index.html')


class ProductListViewTestCase(TestCase):
    fixtures = ['categories.json', 'products.json']

    def test_list_view(self):
        path = reverse('products:index')
        response = self.client.get(path)

        products = Product.objects.all()

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Каталог')
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(tuple(response.context_data['products']), tuple(products[:2]))
