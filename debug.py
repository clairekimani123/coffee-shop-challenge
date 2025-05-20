from customer import Customer
from coffee import Coffee
from order import Order
import unittest
import sys

# Manual testing
def run_manual_tests():
    Order.all = []  # Reset orders
    # Create customers
    alice = Customer("Alice")
    bob = Customer("Bob")
    # Create coffees
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    # Create orders
    order1 = alice.create_order(latte, 5.0)
    order2 = alice.create_order(espresso, 3.5)
    order3 = bob.create_order(latte, 4.5)
    # Test relationships
    print(f"Alice's orders: {len(alice.orders())}")  # Should be 2
    print(f"Alice's coffees: {[coffee.name for coffee in alice.coffees()]}")  # ['Latte', 'Espresso']
    print(f"Latte's customers: {[customer.name for customer in latte.customers()]}")  # ['Alice', 'Bob']
    print(f"Latte's orders: {latte.num_orders()}")  # 2
    print(f"Latte's average price: {latte.average_price()}")  # 4.75
    # Test immutability and validation
    try:
        latte.name = "Mocha"
    except AttributeError as e:
        print(f"Error: {e}")
    try:
        order1.price = 15.0
    except AttributeError as e:
        print(f"Error: {e}")
    try:
        Customer("A" * 16)
    except ValueError as e:
        print(f"Error: {e}")

# Run unit tests
def run_unit_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(__import__('tests.customer_test')))
    suite.addTests(loader.loadTestsFromModule(__import__('tests.coffee_test')))
    suite.addTests(loader.loadTestsFromModule(__import__('tests.order_test')))
    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == '__main__':
    print("Running manual tests:")
    run_manual_tests()
    print("\nRunning unit tests:")
    run_unit_tests()