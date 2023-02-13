from django.test import TestCase
from django.urls import reverse
import django
django.setup()


class IndexViewTestCase(TestCase):

    def test_view(self):
        path = reverse('index')
        response = self.client.get(path)

# DOESNT WORK WITH COMMUNITY VERSION OF PYCHARM
