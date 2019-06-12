from functions import *

def test_add_lists():
    
    assert callable(add_lists)
    
    assert isinstance(add_lists([1,1],[1,1]),list)

test_add_lists()

def test_check_bounds():
    
    assert callable(check_bounds)
    
    assert isinstance(check_bounds([0,0],5), bool)

test_check_bounds()