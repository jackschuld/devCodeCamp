class ShoppingCart:

    def __init__ (self, products):
        self.products = products
        self.price = 0

    
    def add_to_cart(self, product):
        self.products.append(product)
    

    def cart_total(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    
    def empty_cart(self):
        while len(self.products) > 0:
            self.products.pop()
