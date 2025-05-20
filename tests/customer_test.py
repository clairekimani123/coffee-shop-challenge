import pytest
from customer import Customer
from coffee import Coffee
from order import Order

@pytest.fixture
def setup_data():
    Order.all = []
    margeret = Customer("margeret")
    lemmon = Coffee("lemmon")
    latte = Coffee("latte")
    return margeret, lemmon, latte

def test_name_property(setup_data):
    margeret, _, _ = setup_data
    assert margeret.name == "margeret"
    margeret.name = "Margeret"
    assert margeret.name == "Margeret"

def test_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_order(setup_data):
    margeret, lemmon, latte = setup_data
    order1 = Order(margeret, lemmon, 5.0)
    order2 = Order(margeret, latte, 6.0)
    assert len(margeret.orders()) == 2
    assert order1 in margeret.orders()
    assert order2 in margeret.orders()

def test_coffees(setup_data):
    margeret, lemmon, latte = setup_data
    Order(margeret, lemmon, 8.0)
    Order(margeret, latte, 6.0)
    Order(margeret, latte, 6.0)
    coffees = margeret.coffees()
    assert len(coffees) == 2
    assert lemmon in coffees
    assert latte in coffees

def test_create_order(setup_data):
    margeret, lemmon, _ = setup_data
    order = margeret.create_order(lemmon, 5.0)
    assert isinstance(order, Order)
    assert order.customer == margeret
    assert order.coffee == lemmon
    assert order.price == 5.0