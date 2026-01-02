from src.triangle import Triangle
from src.square import Square
from src.rectangle import Rectangle
import pytest

##################--positive add_area--########################
@pytest.mark.parametrize(
    'figure1, figure2, area',
    [
        pytest.param(Triangle(3,4,5), Square(2), 6 + 4, id='triangle + square'),
        pytest.param(Square(5), Rectangle(2,3), 25 + 6, id='square + rectangle'),
        pytest.param(Triangle(6,8,10), Triangle(3,4,5), 24 + 6, id='triangle + triangle'),
    ]
)
def test_add_area_positive(figure1, figure2, area):
    assert figure1.add_area(figure2) == area,f'The sum of areas {figure1.area} + {figure2.area} should be equals {area}'

##################--negative add_area--########################
@pytest.mark.parametrize(
    'figure1, invalid_arg',
    [
        pytest.param(Triangle(3,4,5), "figure", id='triangle + str'),
        pytest.param(Square(5), 123, id='square + int'),
        pytest.param(Rectangle(2,3), None, id='rectangle + None'),
    ]
)
def test_add_area_negative(figure1, invalid_arg):
    with pytest.raises(ValueError):
        figure1.add_area(invalid_arg)
