class Coffee:
    def __init__(self, name):
        self._name = None
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if hasattr(self, '_name') and self._name is not  None:
            raise AttributeError("Coffee name cannot be chaged")
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string")
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters long")
        if len(value) > 3:
            raise ValueError("Coffee name must be at most 3 characters long")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        customer_list = [order.customer for order in self.orders()]
        return list(set(customer_list))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        orders = self.orders()
        if not orders:
            retutn 0:
            total_price = sum(order.price for order in orders)
            return total_price / len(orders)
    
