class Order:
    all = []  # Store all orders

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a Customer instance")
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a Coffee instance")
        self._customer = customer
        self._coffee = coffee
        self.price = price  # Use setter to enforce rules
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if hasattr(self, '_price') and self._price is not None:
            raise AttributeError("Price cannot be changed")
        if not isinstance(value, float):
            raise TypeError("Price must be a float")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0")
        self._price = value

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee