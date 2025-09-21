import pytest
from shifr import shift_words

@pytest.fixture(scope="module", autouse=True)
def before_and_after():
    print("BEGIN")
    yield
    print("END")

def test_shifr():
    assert shift_words("Tree", 3) == "Wuhh"

def test_shifr2():
    assert shift_words("CaLaBaGa Machine2", 7) == "JhShIhNh Thjopul2"

def test_shifr3():
    assert shift_words("Fridrich Iosifovich zaril clad pod fontanom", 5) == "Kwniwnhm Ntxnktanhm efwnq hqfi uti ktsyfstr"

def test_shifr4():
    assert shift_words("Lamadino", 3) != "AbracadabraBums"