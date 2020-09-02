# Test for HDL calculator
import pytest
@pytest.mark.parametrize("Level, expected",[
    (50, "Borderline Low"),
    (70, "Normal"),
    (20, "Low"),
])
def test_HDL_check_ALL(Level,expected):
    from calculator import HDL_check
    result = HDL_check(Level)
    assert result == expected

#def test_HDL_check():
#    from calculator import HDL_check
#    result = [HDL_check(50), HDL_check(70)]
#    expected = ["Borderline Low", "Normal"]
#    assert result == expected

#def test_HDL_check_low():
#    from calculator import HDL_check
#    result = HDL_check(30)
#    expected = ("Low")
#    assert result == expected
