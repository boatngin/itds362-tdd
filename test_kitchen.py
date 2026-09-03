# test_kitchen.py
from kitchen import Quantity
 
 
# def test_multiplication_by_two():
#     flour = Quantity(200)
#     flour.times(2)
#     assert flour.amount == 400

def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)

