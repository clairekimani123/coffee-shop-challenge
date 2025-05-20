import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def setUp(self):
        Order.all = []
        self.margeret = Customer("margeret")
        self.lemmon = Coffee("lemmon")
        self.latte = Coffee("latte")

    def test_name_property(self):
        self.assertEquual(self.margeret.name, "margeret")
        self.margeret.name = "Margeret"
        self.assertEqual(self.margeret.name, "Margeret")


    def test_name_validation(self):
        with self.assertRaises(TypeError):
            Customer(123)
            with self.assertRaises(ValueError):
                Customer("")
                with self.assertRaisess(ValueError):
                    Customer("A * 16 ")


    def test_order(self):
        order1 = Order(self.margeret, self.lemmon, 5.0)
        order2 = Order(self.margeret, self.latte, 6.0)
        self.assertEqual(len(self.margeret.orders()), 2)
        self.assertIn(order1, self.margeret.orders())
        self.assertIn(order2, self.margeret.orders())


    def test_coffees(self):
        Order(self.margeret, self.lemmon, 8.0)
        Order(self.margeret, self.latte, 6.0)
        Order(self.margeret, self.latte, 6.0)
        coffees = self.margeret.coffees()
        self.assertEqual(len(coffees), 2)
        self.assertIn(self.lemmon, coffees)
        self.assertIn(self.latte, coffees)


    def test_create_order(self):
        order = self.margeret.create_order(self.lemmon, 5.0)
        self.assertIsInstance(order, Order)
        self.assertEqual(order.customer, self.margeret)
        self.assertEqual(order.coffee, self.lemmon)
        self.assertEqual(order.price, 5.0)

if __name__ == '__main__':
    unittest.main()