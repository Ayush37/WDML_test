from django.test import TestCase

# Create your tests here.

from .models import CartItem


class PostTestCase(TestCase):
    def test_post(self):
        self.assertEquals(CartItem.objects.count(),0)
        CartItem.objects.create(
            product_name='Test_product1', product_price='37', product_quantity='5', 
        )
        CartItem.objects.create(
            product_name='Test_product2', product_price='73', product_quantity='5',
        )
        self.assertEquals(
            CartItem.objects.count(),
            2
        )
        expensive_posts = CartItem.objects.get(product_price=37)
        self.assertEquals(expensive_posts.product_name,'Test_product1')

