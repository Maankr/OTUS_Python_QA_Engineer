from src.rectangle import Rectangle
import pytest

##############--area positive--#################

@pytest.mark.parametrize(
    'side_a, side_b, area',
    [
        pytest.param(2, 4, 8, id='integer'),
        pytest.param(6, 9, 54, id='integer'),
        pytest.param(3.5, 5.5, 19.25, id='float'),
        pytest.param(10.5, 12.5, 131.25, id='float')
    ]
)
def test_rectangle_positive_area(side_a, side_b, area):
    r = Rectangle(side_a, side_b)
    assert r.area == area, f'The area rectangle with {side_a} and {side_b} should be equals {area}'

#################################################

##############--perimeter positive--#################
@pytest.mark.parametrize(
    'side_a, side_b, perimeter',
    [
        pytest.param(2, 4, 12, id='integer'),
        pytest.param(6, 9, 30, id='integer'),
        pytest.param(3.5, 5.5, 18, id='float'),
        pytest.param(10.5, 12.5, 46, id='float')
    ]
)
def test_rectangle_positive_perimeter(side_a, side_b, perimeter):
    p = Rectangle(side_a, side_b)
    assert p.perimeter == perimeter, f'The perimeter rectangle with {side_a} and {side_b} should be equals {perimeter}'

###################################################

####################--negative test--##############
@pytest.mark.parametrize(
    'side_a, side_b',
    [
        pytest.param(-2, -4, id='integer negative'),
        pytest.param(-6, 9, id='integer negative'),
        pytest.param(-5.5, 0, id='float zero'),
        pytest.param(0, -5.5, id='float zero'),
        pytest.param(0, 0, id='zero'),
    ]
)
def test_rectangle_negative_sides(side_a, side_b):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)

#################################################
