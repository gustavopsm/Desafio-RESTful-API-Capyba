from django.test import TestCase
from ..models import Item

class ItemModelTestCase(TestCase):

    def setUp(self):
        self.Item1 = Item.objects.create(name = 'something1', album = 'something2', explicit = False, duration = 100)

    def test_item_str(self):
        self.assertEquals(self.Item1.__str__(), 'something1')