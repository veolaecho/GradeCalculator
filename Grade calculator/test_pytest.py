
from Calculator import collect_marks

def test_collect_marks_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: " ")
    i = input ("Please enter students mark for module 1: ")
    assert i == " "
