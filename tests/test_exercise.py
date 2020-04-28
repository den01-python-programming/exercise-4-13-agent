import pytest
from src.agent import Agent

def test_exercise(capsys):
    bond = Agent("James", "Bond")
    print(bond)

    ionic = Agent("Ionic", "Bond")
    print(ionic)

    out, err = capsys.readouterr()
    assert out == "My name is Bond, James Bond\nMy name is Bond, Ionic Bond\n"
