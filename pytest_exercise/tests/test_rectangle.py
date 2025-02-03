import pytest


# Test to check the area calculation of the rec_value Rectangle fixture.
def test_area(rec_value):
    # The expected area for a rectangle with length 10 and width 4 is 10 * 4 = 40
    assert rec_value.area() == 10 * 4


# Test to check the perimeter calculation of the rec_value Rectangle fixture.
def test_perimeter(rec_value):
    # The expected perimeter for a rectangle with length 10 and width 4 is 10*2 + 4*2 = 28
    assert rec_value.perimeter() == 10 * 2 + 4 * 2


# Test to verify that two different Rectangle objects are not equal.
def test_not_equal(rec_value, rec_weird):
    # Since rec_value and rec_weird have different dimensions, they should not be equal.
    assert rec_value != rec_weird
