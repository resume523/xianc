import pytest
def setup_function():
    print("DKDL")
def test_failed():
    assert False

def test_passed():
    assert True

def test_failed2():
    assert False
