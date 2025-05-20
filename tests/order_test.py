import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture(autouse=True)
def clear_orders():
    Order._all_orders.clear()

def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("a" * 16)
    c = Customer("Margeret")
    assert c.name == "Margeret"

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("ab")
    c = Coffee("Lemmon")
    assert c.name == "Lemmon"

def test_order_creation_and_properties():
    cust = Customer("Domi")
    cof = Coffee("Mocha")
    order = Order(cust, cof, 5.0)
    assert order.customer is cust
    assert order.coffee is cof
    assert order.price == 5.0

def test_order_price_validation():
    cust = Customer("Domi")
    cof = Coffee("Mocha")
    with pytest.raises(TypeError):
        Order(cust, cof, "expensive")
    with pytest.raises(ValueError):
        Order(cust, cof, 0.5)
    with pytest.raises(ValueError):
        Order(cust, cof, 20.0)

def test_customer_orders_and_coffees():
    margeret = Customer("Margeret")
    domi = Customer("Domi")
    lemmon = Coffee("Lemmon")
    mocha = Coffee("Mocha")
    o1 = margeret.create_order(lemmon, 3.0)
    o2 = margeret.create_order(mocha, 4.0)
    o3 = domi.create_order(lemmon, 5.0)
    assert set(margeret.orders()) == {o1, o2}
    assert set(margeret.coffees()) == {lemmon, mocha}
    assert set(lemmon.customers()) == {margeret, domi}
    assert set(lemmon.orders()) == {o1, o3}

def test_coffee_num_orders_and_average_price():
    margeret = Customer("Margeret")
    domi = Customer("Domi")
    lemmon = Coffee("Lemmon")
    assert lemmon.num_orders() == 0
    assert lemmon.average_price() == 0
    margeret.create_order(lemmon, 4.0)
    domi.create_order(lemmon, 6.0)
    assert lemmon.num_orders() == 2
    assert lemmon.average_price() == 5.0

def test_most_aficionado():
    margeret = Customer("Margeret")
    domi = Customer("Domi")
    lemmon = Coffee("Lemmon")
    mocha = Coffee("Mocha")
    assert Customer.most_aficionado(lemmon) is None
    margeret.create_order(lemmon, 4.0)
    domi.create_order(lemmon, 6.0)
    margeret.create_order(lemmon, 2.0)
    assert Customer.most_aficionado(lemmon) == domi
    margeret.create_order(lemmon, 10.0)
    assert Customer.most_aficionado(lemmon) == margeret
    assert Customer.most_aficionado(mocha) is None