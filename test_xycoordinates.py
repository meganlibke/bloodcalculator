# test
import pytest
@pytest.mark.parametrize("location, xloc, expected", [
    ([(1,2) (3,4)], 2, 3),
])
def test_xyline_coordinates(location,xloc,expected):
    from xycoordinates import xyline_coordinates
    result = xyline_coordinates(location, xloc)
    assert result == expected
