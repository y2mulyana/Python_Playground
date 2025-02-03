import pytest
import source.shapes as shape


@pytest.mark.parametrize("side_length, expected_area",
                         [(5, 25), (4, 16), (3, 9)])
def test_multiple_square_area(side_length, expected_area):
    assert shape.Square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length, expected_perimeter",
                         [(5, 20), (4, 16), (3, 12)])
def test_multiple_square_perimeter(side_length, expected_perimeter):
    assert shape.Square(side_length).perimeter() == expected_perimeter
