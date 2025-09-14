import pytest
from file_utils import program_start, load_data, save_data
from models import Notate

@pytest.fixture(scope="module", autouse=True)
def before_and_after():
    print("BEGIN")
    yield
    print("END")

def test_program_start():
    program_start()


def test_load_data_has_keys():
    data = load_data()
    assert "now_id" in data


def test_save_data_runs():
    data = load_data()
    save_data(data)


def test_notate_has_dict():
    note = Notate(1, "Тест", "2025-09-20", False)
    assert "id" in note.dict
    assert "title" in note.dict
    assert "deadline" in note.dict
    assert "done" in note.dict
