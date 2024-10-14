
import pytest 
from hello import hello

def test_default():
    assert hello() == "Hello, World"
    
def test_argument():
    assert hello("Roy") == "Hello, Roy"