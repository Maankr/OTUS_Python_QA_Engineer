from src.circle import Circle 
import pytest

#############################--positive area--##################
@pytest.mark.parametrize(
    'radius, area',
    [
        pytest.param(13, 530.929158456675, id='integer'),
        pytest.param(2.2, 15.20530844337460215, id='float'),
    ]
)

def test_circle_positive_area(radius, area):
    c = Circle(radius)
    assert c.area == area, f'The area rectangle with radius = {radius} should be equals {area}'

#################--positive perimeter--########################
@pytest.mark.parametrize(
    'radius, perimeter',
    [
        pytest.param(2, 12.566370614359172, id='integer'),
        pytest.param(3.5, 21.991148575128552, id='float'),
    ]
)
def test_circle_positive_perimeter(radius, perimeter):
    c = Circle(radius)
    assert c.perimeter == perimeter, f'The perimeter Circle with radius = {radius} should be equals {perimeter}'

#############################################################

##################--negative--#####################################
@pytest.mark.parametrize(
    'radius',
    [
        pytest.param(-2, id='integer negative'),
        pytest.param(-6, id='integer negative'),
        pytest.param(-5.5, id='float zero'),
        pytest.param(0,id='zero'),
    ]
)
def test_circle_negative_sides(radius):
    with pytest.raises(ValueError):
       Circle(radius)