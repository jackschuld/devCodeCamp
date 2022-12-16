from shopping_cart import ShoppingCart

class Customer:

    def __init__ (self, name):
        self.name = name
        self.cart = ShoppingCart([])
    
    
    def add_to_cart(self, item):
        self.cart.add_to_cart(item)