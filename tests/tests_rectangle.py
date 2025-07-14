import pytest
import source.shapes as shapes

@pytest.fixture
def my_rect():
    return shapes.Rectangle(length = 10, width = 20)

def test_area(my_rect):
    rectangle = my_rect
    assert rectangle.area() == 10 * 20

def test_perimeter(my_rect):
    rectangle = my_rect
    assert rectangle.perimeter() == 2 * (10+20)