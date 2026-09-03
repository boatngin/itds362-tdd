# test_kitchen.py
from kitchen import Quantity,Converter
 
 
# def test_multiplication_by_two():
#     flour = Quantity(200)
#     flour.times(2)
#     assert flour.amount == 400

# def test_equality():
#     assert Quantity(200) == Quantity(200)
#     assert Quantity(200) != Quantity(300)

def test_grams_are_not_ounces():
    assert Quantity(1, "g") != Quantity(1, "oz")


def grams(amount):
    return Quantity(amount, "g")
 
 
def ounces(amount):
    return Quantity(amount, "oz")


def test_simple_addition():
    total = grams(200).plus(grams(300))
    converter = Converter()
    assert converter.reduce(total, "g") == grams(500)
