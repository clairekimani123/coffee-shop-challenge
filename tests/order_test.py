import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        Order.all = []  
        self.margeret = Customer("Margeret")
        self.lemmon = Coffee("Lemmon")

    def test_initializer(self):
        order = Order(self.margeret, self.lemmon, 5.0)
        self.assertEqual(order.customer, self.margeret)
        self.assertEqual(order.coffee, self.lemmon)
        self.assertEqual(order.price, 5.0)

    def test_price_validation(self):
        with self.assertRaises(TypeError):
            Order(self.margeret, self.lemmon, "5")  
        with self.assertRaises(ValueError):
            Order(self.margeret, self.lemmon, 0.5)  
        with self.assertRaises(ValueError):
            Order(self.margeret, self.lemmon, 11.0)

    def test_price_immutability(self):
        order = Order(self.margeret, self.lemmon, 5.0)
        with self.assertRaises(AttributeError):
            order.price = 6.0  

    def test_customer_validation(self):
        with self.assertRaises(TypeError):
            Order("Margeret", self.lemmon, 5.0) 

    def test_coffee_validation(self):
        with self.assertRaises(TypeError):
            Order(self.margeret, "Lemmon", 5.0) 

if __name__ == '__main__':
    unittest.main()