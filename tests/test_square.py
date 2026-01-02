from src.square import Square
import pytest

#############################--positive area--##################
@pytest.mark.parametrize(
    'side_a, area',
    [
        pytest.param(10, 100, id='integer'),
        pytest.param(5.5, 30.25, id='float'),
    ]
)
def test_square_positive_area(side_a, area):
    s = Square(side_a)
    assert s.area == area, f'The area square with side = {side_a} should be equals {area}'

#################--positive perimeter--########################
@pytest.mark.parametrize(
    'side_a, perimeter',
    [
        pytest.param(2, 8, id='integer'),
        pytest.param(5.5, 22, id='float'),
    ]
)
def test_square_positive_perimeter(side_a, perimeter):
    s = Square(side_a)
    assert s.perimeter == perimeter, f'The perimeter square with side = {side_a} should be equals {perimeter}'

##################--negative--##################################
@pytest.mark.parametrize(
    'side_a',
    [
        pytest.param(-2, id='negative integer'),
        pytest.param(0, id='zero'),
        pytest.param(-5.5, id='negative float'),
    ]
)
def test_square_negative_sides(side_a):
    with pytest.raises(ValueError):
        Square(side_a)

