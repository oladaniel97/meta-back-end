from django.test import TestCase
from restaurant.models import *

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='eba',price=20,inventory=150)
        self.assertEqual(item,'eba:20')

class MenuViewTest(TestCase):
    def  setUp(self):
        item = Menu.objects.create(title='eba',price=20,inventory=150)
        
    def test_getall(self):
        items = Menu.objects.all()