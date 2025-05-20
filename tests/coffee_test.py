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

def test_coffee_name_validation():
    with pytest.raises(TypeError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("ab")
    c = Coffee("Lemmon")
    assert c.name == "Lemmon"

def test_coffee_orders_and_customers():
    margeret = Customer("Margeret")
    domi = Customer("Domi")
    lemmon = Coffee("Lemmon")
    mocha = Coffee("Mocha")
    o1 = margeret.create_order(lemmon, 3.0)
    o2 = margeret.create_order(mocha, 4.0)
    o3 = domi.create_order(lemmon, 5.0)
    assert set(lemmon.orders()) == {o1, o3}
    assert set(lemmon.customers()) == {margeret, domi}

def test_num_orders_and_average_price():
    margeret = Customer("Margeret")
    domi = Customer("Domi")
    lemmon = Coffee("Lemmon")
    assert lemmon.num_orders() == 0
    assert lemmon.average_price() == 0
    margeret.create_order(lemmon, 4.0)
    domi.create_order(lemmon, 6.0)
    assert lemmon.num_orders() == 2
    assert lemmon.average_price() == 5.0