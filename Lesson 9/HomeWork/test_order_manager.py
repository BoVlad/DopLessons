from order_manager import new_order, load_data, save_data
import pytest


@pytest.fixture(scope="module", autouse=True)
def before_and_after():
    print("BEGIN")
    yield
    print("END")


def test_new_order():
    assert new_order("Влад", "Телевізор", 2) == True

def test_new_order2():
    assert new_order("Григорій", "Масажер сковорідки", 1) == True

def test_new_order3():
    assert new_order("Алекс", "Фінський пряник", 10) == True