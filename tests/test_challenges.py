#
# To legally & successfully complete the challenges, you MUST NOT change the
# contents of this file!
#

import random

import some_library

_teapot_ret = random.random()
some_library._retval['teapot'] = _teapot_ret

# If you get an error here, then you didn't create a mycode.py
# in the src directory, or there is an error in the file
import mycode

from inspect import cleandoc, getargspec, isfunction, ismodule


#import pytest

#@pytest.fixture()
#def module():
#    import something
#    return something

#
# Starting out
#

def test_s1():
    '''Create a file called `mycode.py` in the `src` directory'''
    pass

#
# Variables
#

def test_v1():
    '''Define a variable named `x`, and make it equal to the number `3`'''
    assert hasattr(mycode, 'x')     # is x defined?
    assert mycode.x == 3            # is x equal to 3

def test_v2():
    assert hasattr(mycode, 's')         # is s defined?
    assert isinstance(mycode.s, str)    # is it a string?
    assert mycode.s == 'I am a string'  # correct value?

def test_v3():
    '''Define a variable named `b`, and make it equal to the boolean false value'''
    assert hasattr(mycode, 'b')         # is b defined?
    assert mycode.b is False            # is it False?

#
# Functions
#

def test_f1():
    '''Define a function called `do_something`'''
    assert isfunction(mycode.do_something)  # is there a function called 'do something'?

def test_f2():
    '''`do_something` should take two parameters, `x1` and `x2`'''
    
    (args, varargs, keywords, defaults) = getargspec(mycode.do_something)
    
    assert len(args) == 2           # check that there are two parameters
    assert args[0] == 'x1'          # check for a parameter called 'x1'
    assert args[1] == 'x2'          # check for a parameter called 'x2'

def test_f3():
    '''`do_something` should have a docstring that says "This does something"'''
    
    docstring = mycode.do_something.__doc__
    assert docstring is not None                        # does it have a docstring?
    assert cleandoc(docstring) == 'This does something' # check the docstring contents
    
def test_f4():
    '''`do_something` should return the result of `x1` times `x2`'''
    
    assert mycode.do_something(2, 2) == 4      # 2 times 2 is 4
    
    for i in range(0, 10):
        for j in range(0, 10):
            assert mycode.do_something(i, j) == i*j     # does it return an expected result?

def test_f5():
    '''Define a function called `keyword_fn`, it should take a keyword argument
       called `keyword`, with a default value of `None`'''
    
    assert hasattr(mycode, 'keyword_fn')    # does `keyword_fn` exist
    assert isfunction(mycode.keyword_fn)    # is `keyword_fn` a function?
    
    (args, varargs, keywords, defaults) = getargspec(mycode.keyword_fn)
    
    print(args, varargs, keywords, defaults)
    assert args[0] == 'keyword'             # first arg should be 'keyword'
    assert defaults[0] == None              # default should be None
    

def test_f6():
    '''If `keyword` is None, then `keyword_fn` should return the string 'No'.
       Otherwise, it should return the keyword argument plus `2`'''
    
    assert mycode.keyword_fn() == 'No'          # return No if no arg
    assert mycode.keyword_fn(keyword=2) == 4    # return arg + 2
    
    for arg in range(90):
        assert mycode.keyword_fn(arg) == arg + 2    # return arg + 2


def test_f7():
    '''Define a function called `return_many`, it should take three parameters'''
    
    assert hasattr(mycode, 'return_many')     # does `return_things` exist
    assert isfunction(mycode.return_many)     # is `return_things` a function?
     
    (args, varargs, keywords, defaults) = getargspec(mycode.return_many)
    
    assert len(args) == 3   # does `return_things` take two parameters?


def test_f8():
    '''`return_many` should add '2' to each of the parameters, and return the
       three parameters as a tuple'''
    
    assert isinstance(mycode.return_many(1,2,3), tuple) # return value should be a tuple
    
    for arg1 in range(50):
        for arg2 in range(50):
            for arg3 in range(50):
                assert mycode.return_many(arg1, arg2, arg3) == (arg1+2, arg2+2, arg3+2)   # is math correct?

def test_f9():
    '''Call `return_many` with the parameters 1, 2, and 3, and assign the returned
       values to the variables r1, r2, and r3'''
    
    assert mycode.r1 == 3
    assert mycode.r2 == 4
    assert mycode.r3 == 5

#
# Modules
#

def test_m1():
    '''Import the library called `some_library`'''
    
    assert hasattr(mycode, 'some_library')      # is some_library in the module?
    assert ismodule(mycode.some_library)        # is it a module?
    assert mycode.some_library is some_library  # is it the same module? 
    
def test_m2():
    '''Call the `i_am_a_teapot` function inside of `some_library`, store its
       return value in a variable called `teapot`'''
       
    assert some_library._called['teapot'] == True   # if not True, the i_am_a_teapot function was never called
       
    assert hasattr(mycode, 'teapot')        # is teapot defined?
    assert mycode.teapot is _teapot_ret     # is it the expected value?

def test_m3():
    '''Define a function called `gonna_call_stuff`, and have it take a
       single parameter'''
    
    assert isfunction(mycode.gonna_call_stuff)  # is there a function called 'gonna_call_stuff'?
    (args, varargs, keywords, defaults) = getargspec(mycode.gonna_call_stuff)
    
    assert len(args) == 1   # does `gonna_call_stuff` take a single parameter?
    
    
def test_m4():
    '''From the `gonna_call_stuff` function, call the `multiply_by_2` function
      in the `some_library` library with the first parameter equal to the first
      parameter of the `gonna_call_stuff` function, and return the value returned by
      `multiply_by_2`'''
    
    assert mycode.gonna_call_stuff(999) == 999*3        # see if gonna_call_stuff returns the right value
    assert some_library._called['multiply'] == True     # If not true, the multiply_by_2 function wasn't called

#
# Classes & Objects
#

# TODO

#
# Exceptions
#

# TODO

