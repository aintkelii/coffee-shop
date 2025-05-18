from customer import Customer
from coffee import Coffee

trevour = Customer("George")
joy = Customer("muli")

espresso = Coffee("bacardi")
latte = Coffee("juice")

trevour.create_order(espresso, 4.0)
joy.create_order(latte, 5.5)
trevour.create_order(latte, 3.5)

print(f"Created customers: {trevour.name}, {joy.name}")
print(f"{espresso.name} has {espresso.num_orders()} orders.")
print(f"{latte.name} average price: {latte.average_price():.2f}")

