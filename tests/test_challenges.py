
# If you get an error here, then you didn't create a mycode.py
# in the src directory, or there is an error in the file
import mycode

from inspect import cleandoc, getargspec, isfunction


#import pytest

#@pytest.fixture()
#def module():
#    import something
#    return something

def test_1():
    '''Create a file called `mycode.py` in the `src` directory'''
    pass

def test_2():
    '''Define a variable named `x`, and make it equal to the number `3`'''
    assert hasattr(mycode, 'x')     # is x defined?
    assert mycode.x == 3            # is x equal to 3

def test_3():
    '''Define a function called `do_something`'''
    assert isfunction(mycode.do_something)  # is there a function called 'do something'?

def test_4():
    '''`do_something` should take two parameters, `x1` and `x2`'''
    
    (args, varargs, keywords, defaults) = getargspec(mycode.do_something)
    
    assert len(args) == 2           # check that there are two parameters
    assert args[0] == 'x1'          # check for a parameter called 'x1'
    assert args[1] == 'x2'          # check for a parameter called 'x2'

def test_5():
    '''`do_something` should have a docstring that says "This does something"'''
    
    docstring = mycode.do_something.__doc__
    assert docstring is not None                        # does it have a docstring?
    assert cleandoc(docstring) == 'This does something' # check the docstring contents
    
def test_6():
    '''`do_something` should return the result of `x1` times `x2`'''
    
    assert mycode.do_something(2, 2) == 4      # 2 times 2 is 4
    
    for i in range(0, 10):
        for j in range(0, 10):
            assert mycode.do_something(i, j) == i*j     # does it return an expected result?
    
