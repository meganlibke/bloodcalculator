# test
import pytest
@pytest.mark.parametrize("coords, slope, offset", [
    ([(1,2), (3,4)], 1, 1),
    ([(9,2),(7,4)], -1, 11),
])
def test_xyline_coordinates(coords,slope,offset):
    from xycoordinates import xyline_coordinates
    result = xyline_coordinates(coords)
    assert result == (slope, offset)

@pytest.mark.parametrize("slope, offset, xloc, yloc", [
    (1, 1, 2, 3),
    (-1, 11, 8, 3),
])
def test_new_location(slope,offset,xloc,yloc):
    from xycoordinates import new_location
    result = new_location(slope,offset,xloc)
    assert result == yloc
