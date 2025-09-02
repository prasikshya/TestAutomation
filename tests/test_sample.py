import pytest

def test_addition():
    assert 2 + 3 == 5

def test_subtraction():
    assert 5 - 3 == 2

@pytest.mark.parametrize("a,b,result", [(2,3,5), (5,5,10)])
def test_parametrized_add(a, b, result):
    assert a + b == result

