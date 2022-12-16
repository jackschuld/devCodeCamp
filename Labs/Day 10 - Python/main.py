from alarm_clock import AlarmClock
from product import Product
from customer import Customer

customer = Customer('Jack')
clock = AlarmClock('1:50', True, '2:00')
apple = Product('Apple', 0.33, 'Fruits')
banana = Product('Banana', 0.70, 'Fruits')
orange = Product('Orange', 0.31, 'Fruits')


customer.add_to_cart(apple)
customer.add_to_cart(banana)
customer.add_to_cart(orange)

print(customer.cart.cart_total())

# print(cart.products)
# cart.empty_cart()
# print(cart.products)

# clock.print_time()

# clock.set_current_time('1:55')

# clock.toggle_on_or_off() # OFF

# clock.print_time() # Nothing to terminal

# clock.toggle_on_or_off() # ON

# clock.print_time() # 1:55


