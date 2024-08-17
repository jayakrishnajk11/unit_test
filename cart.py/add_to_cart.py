class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Quantity:", self.quantity)


class Cart:
    def __init__(self, user_name):
        self.user_name = user_name
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)
        print("Product added to cart")

    def remove_from_cart(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                print("Product removed from cart")
                return
        print("Product not found in cart")

    def display_cart(self):
        print("Cart contents for", self.user_name)
        if not self.products:
            print("Cart is empty")
        else:
            for product in self.products:
                product.display_info()


def cart_products():
    product1 = Product("Shirt", 499, 2)
    product2 = Product("Pant", 699, 1)
    cart = Cart("Jaya")
    cart.add_to_cart(product1)
    cart.add_to_cart(product2)
    cart.display_cart()
    cart.remove_from_cart("Shirt")
    cart.display_cart()


cart_products()