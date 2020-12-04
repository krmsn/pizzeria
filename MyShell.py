import os
import django
from pizzas.models import pizza

os.environment.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

django.setup()

pizzas = Pizza.objects.all()

for pizza in pizzas:
    print(pizza.id, pizza)

p = Pizza.objects.get(id = 1)
print(p.name)

# set.all() calls every topping when a pizza is opened
toppings = p.topping_set.all()

for topping in toppings:
    print(topping)
