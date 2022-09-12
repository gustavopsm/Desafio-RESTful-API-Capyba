from django.test import TestCase
from ..models import ItemPrivado

class ItemPrivadoModelTestCase(TestCase):

    def setUp(self):
        self.Itemprivado1 = ItemPrivado.objects.create(name = 'something1', album = 'something2', explicit = False, duration = 100)

    def test_itemprivado_str(self):
        self.assertEquals(self.Itemprivado1.__str__(), 'something1')