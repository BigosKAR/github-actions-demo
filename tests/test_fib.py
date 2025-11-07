import pytest
from main import fib

def test_fib_base_cases():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5

def test_fib_larger():
    # known value: fib(50) = 12586269025
    assert fib(50) == 12586269025

# def test_negative_raises():
#     with pytest.raises(ValueError):
#         TODO

# def test_type_error():
#     with pytest.raises(TypeError):
#         TODO