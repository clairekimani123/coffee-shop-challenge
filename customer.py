class Customer: 
    def __init__(self, name):
        self.name = name  # Use the setter to enforce rules

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(value) <= 15):
            raise ValueError("Name must be between 1 and 15 characters")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        # Get unique coffees from this customer's orders
        coffee_list = [order.coffee for order in self.orders()]
        return list(set(coffee_list))

    def create_order(self, coffee, price):
        return Order(self, coffee, price)