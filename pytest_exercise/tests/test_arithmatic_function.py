import pytest
import source.arithmatic_function as af


def test_add():
    result = af.add(x=1, y=4)
    assert result == 5


def test_add_string():
    result = af.add(x="Become better ", y="everyday")
    assert result == "Become better everyday"


def test_divide():
    result = af.divide(x=10, y=5)
    assert result == 2


def test_divide_zero():
    with pytest.raises(ValueError):
        af.divide(x=5, y=0)


@pytest.mark.skip(reason="This feature still broken")
def test_skip():
    assert af.add(x=12, y=3)


@pytest.mark.xfail(reason="It will be failed")
def test_failed():
    af.divide(x=13, y=0)
