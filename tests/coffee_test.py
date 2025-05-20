import unittest
from customer import Customer
from coffee import coffee
from order import Order

class TestCoffee(unittest.TestCase):
        def setUp(self):
                Order.all = []
                self.margeret = Customer("Margret")
                self.bob = Customer("Bob")
                self.lemmon = Coffee("lemmon")

        def test_name_property(self):
            self.assertEqual(self.lemmon.name, "Lemmon")
            with self.assertRaises(AttributeError):
                self.lemmon.name = "Mocha"  

        def test_name_validation(self):
            with self.assertRaises(TypeError):
             Coffee(123)  
            with self.assertRaises(ValueError):
                Coffee("Ab") 



        def test_orders(self):
            order1 = Order(self.margeret, self.lemmon, 8.0)
            order2 = Order(self.bob, self.lemmon, 7.0)
            self.assertEqual(len(self.lemmon.orders()), 2)
            self.assertIn(order1, self.lemmon.orders())
            self.assertIn(order2, self.lemmon.orders())


        def test_customer(self):
             Order(self.margeret, self.lemmon, 8.0)
             Order(self.bob, self.lemmon, 7.0)
             Order(self.margeret, self.lemmon, 7.0)
             customer = self.lemmon.customers()
             self.assertEqual(len(customer), 2)
             self.assertIn(self.margeret, customers)
        self.assertIn(self.bob, customers)


        def test_num_orders(self):
             self.assertEqual(self.lemmon.num_orders(), 0)
             Order(self.margeret, self.lemmon, 8.0)
             Order(self.bob, self.lemmon, 7.0)
             self.assertEqual(self.lemmon.num_orders(), 2)


        def test_average_price(self):
             self.assertEqual(self.lemmon.average_price(), 0)
             Order(self.margeret, self.lemmon, 8.0)
             Order(self.bob, self.lemmon, 7.0)
             self.assertEqual(self.lemmon.average_price(), 7.5)
        def test_create_order(self):
             order = self.lemmon.create_order(self.margeret, 5.0)
             self.assertIsInstance(order, Order)
             self.assertEqual(order.customer, self.margeret)
             self.assertEqual(order.coffee, self.lemmon)
             self.assertEqual(order.price, 5.0)
             
if __name__ == '__main__':
     unittest.main()
             
             
