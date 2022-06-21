from cusorder.customer import Customer
from cusorder.order import Order

j1 = Customer('Jame','Nontaburi')
j2 = Order('15-06-2022','packed')
print(f'Order of {j1.name} on {j2.date} in {j2.status}')