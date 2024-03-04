from django.test import TestCase
from myapp.models import Item

# Create your tests here.

class ItemTestCase(TestCase):

    def initial(self):
        Item.objects.create(name="test")

    # This will serve as an example for future testing.
    def test_str_example(self):
        item = Item.objects.get(name="test")
        self.assertEqual(str(item), "test")