import pytest
from main_logic import find_first_unique_char

@pytest.fixture(scope="module", autouse=True)
def before_and_after():
    print("BEGIN")
    yield
    print("END")

def test_find_first_unique_char():
    assert find_first_unique_char("abbbccdf") == "a"

def test_find_first_unique_char2():
    assert find_first_unique_char("aabbcdeeff") == "c"

def test_find_first_unique_char3():
    assert find_first_unique_char("aabbcc") is None