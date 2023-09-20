import pytest
from some_project import main


def test_main():
    assert main() == 'Good night'
