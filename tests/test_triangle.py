from src.triangle import Triangle
import pytest

###################--fixture--###################################
@pytest.fixture
def triangle_3_4_5():
    return Triangle(3, 4, 5)

def test_triangle_area(triangle_3_4_5):
    assert triangle_3_4_5.area == 6

def test_triangle_perimeter(triangle_3_4_5):
    assert triangle_3_4_5.perimeter == 12

################################################################

#############################--positive area--##################
@pytest.mark.parametrize(
    'side_a, side_b, side_c, area',
    [
        pytest.param(3, 4, 5, 6, id='integer'),
        pytest.param(6, 8, 10, 24, id='float'),
        pytest.param(5, 5, 6, 12, id='int'),
    ]
)

def test_triangle_positive_area(side_a, side_b, side_c, area):
    c = Triangle(side_a, side_b, side_c)
    assert c.area == area, f'The area triangle with side = {side_a}, {side_b}, {side_c} should be equals {area}'

#################--positive perimeter--########################
@pytest.mark.parametrize(
    'side_a, side_b, side_c, perimeter',
    [
        pytest.param(3,4,5,12, id='integer'),
        pytest.param(5,5,6,16, id='float')
    ]
)
def test_triangle_positive_perimeter(side_a, side_b, side_c, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.perimeter == perimeter, f'The perimeter triangle with side = {side_a}, {side_b} should be equals {perimeter}'

#############################################################

##################--negative--#####################################
@pytest.mark.parametrize(
    'side_a, side_b, side_c',
    [
        pytest.param(-1, 2, 3,  id='integer negative'),
        pytest.param(3, -2, 3,  id='integer negative'),
        pytest.param(3, 4, -5, id='float zero'),
        pytest.param(0, 4, 5, id='zero'),
        pytest.param(1,2,3, id='impossible')
    ]
)
def test_triangle_negative_sides(side_a, side_b, side_c):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)