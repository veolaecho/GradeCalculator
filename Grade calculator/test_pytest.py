# testing collect_marks function
from Calculator import collect_marks

def test_collect_marks_input(monkeypatch): #passed
    monkeypatch.setattr('builtins.input', lambda _: " ")
    i = input ("Please enter students mark for module 1: ")
    assert i == " "

def test_collect_marks_input2(monkeypatch): #passed
    monkeypatch.setattr('builtins.input', lambda _: "ab")
    i = input ("Please enter students mark for module 2: ")
    assert i == "ab"

def test_collect_marks_input3(monkeypatch): #passed
    monkeypatch.setattr('builtins.input', lambda _: "#@")
    i = input ("Please enter students mark for module 3: ")
    assert i == "#@"

def test_collect_marks_input4(monkeypatch): #pased
    monkeypatch.setattr('builtins.input', lambda _: "9v")
    i = input ("Please enter students mark for module 4: ")
    assert i == "9v"

def test_collect_marks_input5(monkeypatch):#passed
    monkeypatch.setattr('builtins.input', lambda _: "-5m")
    i = input ("Please enter students mark for module 5: ")
    assert i == "-5m"

def test_collect_marks6(monkeypatch):
    inputs = iter(['30', '40', '50', '60', '70'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = collect_marks()
    assert result == "30, 40, 50, 60, 70"