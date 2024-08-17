import unittest
from add_to_cart import Cart, Product

class TestAddToCart(unittest.TestCase):

    def test_add_single_product(self):
        cart = Cart("Jaya")
        product = Product("Shirt", 499, 2)
        cart.add_to_cart(product)
        self.assertEqual(len(cart.products), 1)
        self.assertEqual(cart.products[0].name, "Shirt")

    def test_add_multiple_products(self):
        cart = Cart("Jaya")
        product1 = Product("Shirt", 499, 2)
        product2 = Product("Pant", 699, 1)
        cart.add_to_cart(product1)
        cart.add_to_cart(product2)
        self.assertEqual(len(cart.products), 2)
        self.assertEqual(cart.products[0].name, "Shirt")
        self.assertEqual(cart.products[1].name, "Pant")

    def test_add_same_product_twice(self):
        cart = Cart("Jaya")
        product = Product("Shirt", 499, 2)
        cart.add_to_cart(product)
        cart.add_to_cart(product)
        
if __name__ == '__main__':
    unittest.main()


