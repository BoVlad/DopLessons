from calculator import add
import pytest

@pytest.fixture(scope="module", autouse=True)
def before_and_after():
    print("BEGIN")
    yield
    print("END")


def test_add():
    assert add(2, 3) == 5

def test_add2():
    assert add(10, 5) == 15

def test_add3():
    assert add(3, 3) == 6