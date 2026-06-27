class Pizza:
    def __init__(self, size, cheese, toppings):
        self.size = size
        self.cheese = cheese
        self.toppings = toppings

    def __str__(self):
        return f"Pizza(size={self.size}, cheese={self.cheese}, toppings={self.toppings})"


class PizzaBuilder:
    def __init__(self):
        self.size = "medium"
        self.cheese = False
        self.toppings = []

    def set_size(self, size):
        self.size = size
        return self

    def add_cheese(self):
        self.cheese = True
        return self

    def add_topping(self, topping):
        self.toppings.append(topping)
        return self

    def build(self):
        return Pizza(
            size=self.size,
            cheese=self.cheese,
            toppings=self.toppings
        )


pizza = (
    PizzaBuilder().set_size("large").add_cheese().add_topping("onion")
    .add_topping("capsicum")
    .build()
)

print(pizza)
print(pizza.size)
print(pizza.toppings)