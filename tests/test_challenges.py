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

from inspect import cleandoc, getargspec, isclass, isfunction, ismethod, ismodule
import pytest

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
# Tuples
#

def test_t1():
    '''Define a variable `t1`, and make it equal to an empty tuple'''

    assert isinstance(mycode.t1, tuple)     # is it a tuple?
    assert len(mycode.t1) == 0              # it shouldn't have any elements

def test_t2():
    '''Define a variable `t2`, and make it equal to a tuple containing the value False'''

    assert isinstance(mycode.t2, tuple)     # is it a tuple?
    assert len(mycode.t2) == 1              # tuple of length 1
    assert mycode.t2[0] is False            # 0th element is False

def test_t3():
    '''Define a variable `t3`, and make it equal to a tuple containing 32000 elements'''

    assert isinstance(mycode.t3, tuple)     # is it a tuple?
    assert len(mycode.t3) == 32000          # is it 32000 elements long?

def test_t4():
    '''Define a variable `t4`, and make it equal to a tuple containing the values 'foo', 1,
       and False in it (in that order).'''

    assert isinstance(mycode.t4, tuple)     # is it a tuple?
    assert mycode.t4[0] == 'foo'            # check 0th element
    assert mycode.t4[1] is 1                # check 1st element
    assert mycode.t4[2] is False            # check 2nd element

def test_t5():
    '''Define a variable `t5`, and make it equal to the 0th element of `t4`'''

    assert mycode.t5 is mycode.t4[0]        # t must be equal to the 0th element of t4

def test_t6():
    '''Define a function called `measure_tuple`, that takes a single parameter'''

    assert isfunction(mycode.measure_tuple)  # is there a function called 'measure_tuple'?
    (args, varargs, keywords, defaults) = getargspec(mycode.measure_tuple)
    
    assert len(args) == 1   # does `measure_tuple` take a single parameter?


def test_t7():
    '''`measure_tuple` should return the number of elements present in the tuple'''

    assert mycode.measure_tuple(()) == 0

    for i in range(10):
        assert mycode.measure_tuple((True,)*i) == i


def test_t8():
    '''Define a function called `sum_tuple`, that takes a single parameter'''

    assert isfunction(mycode.sum_tuple)  # is there a function called 'sum_tuple'?
    (args, varargs, keywords, defaults) = getargspec(mycode.sum_tuple)
    
    assert len(args) == 1   # does `sum_tuple` take a single parameter?

def test_t9():
    '''In `sum_tuple`, the parameter is a tuple. If there are 5 elements in
       the tuple, return the sum of the elements in the tuple. Otherwise, return None.'''

    assert mycode.sum_tuple(()) == None
    assert mycode.sum_tuple((1,)) == None
    assert mycode.sum_tuple((1,2,3,4,)) == None
    assert mycode.sum_tuple((1,)*3000) == None
    assert mycode.sum_tuple((1,2,3,4,5)) == 15
    
#
# Lists
#

def test_l1():
    '''Define a variable `l1`, and make it equal to an empty list'''

    assert isinstance(mycode.l1, list)      # is it a list?
    assert len(mycode.l1) == 0              # it shouldn't have any elements

def test_l2():
    '''Define a variable `l2`, and make it equal to a list containing the value False'''

    assert isinstance(mycode.l2, list)     # is it a list?
    assert len(mycode.l2) == 1              # list of length 1
    assert mycode.l2[0] is False            # 0th element is False

def test_l3():
    '''Define a variable `l3`, and make it equal to a list containing 32000 elements'''

    assert isinstance(mycode.l3, list)      # is it a list?
    assert len(mycode.l3) == 32000          # is it 32000 elements long?

def test_l4():
    '''Define a variable `l4`, and make it equal to a list containing the values 'foo', 1,
       and False in it (in that order).'''

    assert isinstance(mycode.l4, list)      # is it a list?
    assert mycode.l4[0] == 'foo'            # check 0th element
    assert mycode.l4[1] is 1                # check 1st element
    assert mycode.l4[2] is False            # check 2nd element

def test_l5():
    '''Define a variable `l5`, and make it equal to the 0th element of `l4`'''

    assert mycode.l5 is mycode.l4[0]        # l5 must be equal to the 0th element of l4

def test_l6():
    '''Define a function called `measure_list`, that takes a single parameter'''

    assert isfunction(mycode.measure_list)  # is there a function called 'measure_list'?
    (args, varargs, keywords, defaults) = getargspec(mycode.measure_list)
    
    assert len(args) == 1   # does `measure_list` take a single parameter?


def test_l7():
    '''`measure_list` should return the number of elements present in the list'''

    assert mycode.measure_list(()) == 0

    for i in range(10):
        assert mycode.measure_list((True,)*i) == i


def test_l8():
    '''Define a function called `sum_list`, that takes a single parameter'''

    assert isfunction(mycode.sum_list)  # is there a function called 'sum_list'?
    (args, varargs, keywords, defaults) = getargspec(mycode.sum_list)
    
    assert len(args) == 1   # does `sum_list` take a single parameter?

def test_l9():
    '''In `sum_list`, the parameter is a list. If there are 5 elements in
       the list, return the sum of the elements in the list. Otherwise, return None.'''

    assert mycode.sum_list(()) == None
    assert mycode.sum_list((1,)) == None
    assert mycode.sum_list((1,2,3,4,)) == None
    assert mycode.sum_list((1,)*3000) == None
    assert mycode.sum_list((1,2,3,4,5)) == 15


def test_l10():
    '''Define a function called `wopit` that takes a single parameter, and
      returns None. The parameter is a list. Add the first element of the list to the
      end of the list. Do nothing if the list is empty.'''

    x = random.random()
    l10_1 = [x, 2, 3]
    mycode.wopit(l10_1)
    assert l10_1 == [x, 2, 3, x]

    l10_2 = []
    mycode.wopit(l10_2)
    assert l10_2 == []

def test_l11():
    '''Define a function called `bopit` that takes a single parameter, and
       returns None. The parameter is a list. Remove an item from the end of the list.
       Do nothing if the list is empty.'''

    l11_1 = [1,2,3]
    mycode.bopit(l11_1)
    assert l11_1 == [1,2]

    l11_2 = []
    mycode.bopit(l11_2)
    assert l11_2 == []

def test_l12():
    '''Define a function called `mopit` that takes a single parameter, and
       returns None. The parameter is a list. Remove an item from the beginning
       of the list. Do nothing if the list is empty.'''

    l12_1 = [1,2,3]
    mycode.mopit(l12_1)
    assert l12_1 == [2,3]

    l12_2 = []
    mycode.mopit(l12_2)
    assert l12_2 == []

def test_l13():
    '''Define a function called `zopit` that takes a single parameter. The
       parameter is a list. Return True if there is an element in the list that is
       equal to the string `item`, and the element position in the list is greater
       than 100. Otherwise, return False.'''

    for list_len in range(200):
        for pos_item in range(list_len):
            l = [False] * list_len

            # for giggles, sometimes the item isn't there
            has_item = (pos_item % 2 == 0)
            if has_item:
                l[pos_item] = 'item'

            r = mycode.zopit(l)

            if has_item and pos_item > 100:
                assert r is True
            else:
                assert r is False

#
# Dictionaries
#

def test_d1():
    '''Define a variable `d1`, and make it equal to an empty dictionary'''

    assert isinstance(mycode.d1, dict)      # is it a dictionary?
    assert len(mycode.d1.keys()) == 0       # is it empty?

def test_d2():
    '''Define a variable `d2`, ane make it a dictionary with the following
    key/value pairs: key: 'k1', value: 'item'; key: 'k2', value: a tuple with
    the elements 1 and 2. '''

    assert isinstance(mycode.d2, dict)      # is it a dictionary?
    assert mycode.d2.get('k1') == 'item'    # k1 is an item?

    t = mycode.d2.get('k2')                 # k2 is a tuple?
    assert isinstance(t, tuple)
    assert len(t) == 2
    assert t[0] is 1
    assert t[1] is 2

def test_d3():
    '''Define a variable `d3` that is equal to the value stored in the
    dictionary with key `k2`'''

    assert mycode.d3 is mycode.d2.get('k2')

def test_d4():
    '''Define a function called `superd` that takes a single parameter. The
      parameter is a dictionary. Add 10000 elements to the dictionary, with the
      keys numbers 1 - 10000. The values associated with each key is the key as
      a string value.'''

    d = dict()
    mycode.superd(d)

    assert len(d) == 10000      # does the dictionary have the right number of elements?

    for i in range(1, 10000):
        assert i in d           # does the key exist?
        assert d[i] == '%s' % i # is is the right value?


#
# Classes & Objects
#

def test_c1():
    '''Define a class called `MyClass`'''

    assert isclass(mycode.MyClass)  # has the class been defined?

def test_c2():
    '''Add a class variable to `MyClass` called `clsvar`, equal to the value 3'''

    assert hasattr(mycode.MyClass, 'clsvar')  # class variable exist?
    assert mycode.MyClass.clsvar is 3         # is it 3?

def test_c3():
    """Define a constructor method for `MyClass`, taking a single parameter.
       The parameter must be set as an instance variable (also called an 'attribute')
       called 'instvar'. If the parameter is equal to the string 'Hi', then the
       'instvar' attribute must be set to 'Hello'"""

    assert not hasattr(mycode.MyClass, 'instvar') # make sure it's not a class variable

    # check to see if instructions were followed
    for i in range(10):
        m = mycode.MyClass(i)
        assert m.instvar == i

    m = mycode.MyClass('Hi')
    assert m.instvar == 'Hello'     # Follow instructions?

def test_c4():
    '''In `MyClass`, define a method called 'add5', which takes a single
      parameter. The method must add the number 5 to the parameter, and add the
      result to the instance parameter 'instvar'. If `instvar` is greater than
      100, the method must return True. Return False otherwise.'''

    assert isfunction(mycode.MyClass.add5)    # does add5 exist and is a method?

    m1 = mycode.MyClass(0)

    r = m1.add5(5)
    assert r == False               # check result
    assert m1.instvar == 10         # check that the operation happened

    r = m1.add5(86)
    assert r == True                # check result
    assert m1.instvar == 101        # check that the operation happened

    r = m1.add5(0)
    assert r == True                # check result
    assert m1.instvar == 106        # check that the expected operation happened

    # Here's a better test
    for i in range(100):
        for j in range(100):
            m2 = mycode.MyClass(i)
            r = m2.add5(j)

            assert m2.instvar == i + j + 5 # first check the value

            # next check the result
            if i + j + 5 > 100:
               assert r == True
            else:
                assert r == False

def test_c5():
    '''In `MyClass`, define a property method called `prop` which must always
       return the string 'hi'.'''

    assert hasattr(mycode.MyClass, 'prop')              # does the 'prop' property exist?
    assert isinstance(mycode.MyClass.prop, property)    # is it a property?

    m = mycode.MyClass(1)
    assert m.prop == 'hi'

def test_c6():
    '''In `MyClass`, when the `prop` property is set, it must set an instance
       variable called '_prop' to the value it was set to'''

    assert hasattr(mycode.MyClass, 'prop')              # does the 'prop' property exist?
    assert isinstance(mycode.MyClass.prop, property)    # is it a property?

    m = mycode.MyClass(1)
    assert m.prop == 'hi'
    m.prop = 1234
    assert hasattr(m, '_prop')      # did the value get set to the correct attribute?
    assert m._prop == 1234          # is the value of _prop correct?
    assert m.prop == 'hi'

    # serious testing
    for i in range(10000):
        m = mycode.MyClass(1)
        m.prop = i
        assert m._prop == i

def test_c7():
    '''In `MyClass`, define two functions, `a` (taking a single parameter)
       and `b` (taking no parameters). When `b` is called, it must return the value
       that was passed to the `a` function. If the `a` function was never called,
       `b` must return None. '''

    m1 = mycode.MyClass(1)

    val = 'string'
    m1.a(val)
    assert m1.b() is val     # make sure the return value is correct

    m2 = mycode.MyClass(2)
    assert m2.b() == None    # did you follow the rules?

    for i in range(10000):        
        m1.a(i)
        assert m1.b() == i   # make sure the return value is correct



def test_c8():
    '''Create an instance of `MyClass` and assign it to a variable called
      `mine`. Create another instance of `MyClass` and assign it to a variable
      called `mine2`'''

    assert hasattr(mycode, 'mine')
    assert hasattr(mycode, 'mine2')

    assert isinstance(mycode.mine, mycode.MyClass)  # is it an instance?
    assert isinstance(mycode.mine2, mycode.MyClass) # is it an instance?

    assert mycode.mine is not mycode.mine2  # not the same instance
    assert mycode.mine.instvar is mycode.mine.instvar # must be the same exact string



#
# State Machine
#

def test_sm1():
    '''Define a class called `StateMachine`'''

    assert isclass(mycode.StateMachine)     # has the class been defined?

def test_sm2():
    '''The constructor for `StateMachine` will receive a single argument,
       which is a string indicating which state to start in. A readonly property
       of the `StateMachine` class called `state` must be defined, which will
       return the string representing the current state.'''

    assert isinstance(mycode.StateMachine.state, property)

    sm = mycode.StateMachine('init')
    assert sm.state == 'init'

    with pytest.raises(AttributeError):
        sm.state = 'foo'         # make sure the property can't be written

    # try a bunch of random states
    for i in range(10000):
        sm = mycode.StateMachine(str(i))
        assert sm.state == str(i)


def test_sm3():
    '''Define a method of `StateMachine` called `reset`. If this method
       is called, the current state must be set to the 'init' state.'''

    for i in range(10000):
        sm = mycode.StateMachine(str(i))
        assert sm.state == str(i)

        sm.reset()
        assert sm.state == 'init'

    # test this once
    
def run_the_test(sm, initial_state):
    '''function to test the state machine'''

    assert sm.state == initial_state

    # test the initial state
    if initial_state == 'init':
        for i in range(10):
            ret = sm.process(False)
            assert ret == False
            assert sm.state == 'init'

            yield

        # test the running state
        ret = sm.process(True)
        assert ret == True

    if initial_state in ['init', 'running']:
        assert sm.state == 'running'

        for i in range(19):
            if i % 2 == 0:
                param = True
            else:
                param = False

            ret = sm.process(param)

            assert sm.state == 'running'    
            assert ret == True              # when running, always True

            yield

        ret = sm.process(True)
        assert ret == True
        assert sm.state == 'slowing'

    # test the slowing state
    for i in range(9):
        if i % 2 == 0:
            param = True
        else:
            param = True

        ret = sm.process(param)

        assert sm.state == 'slowing'
        assert ret == True

        yield

    ret = sm.process(True)
    assert sm.state == 'init'   # did it reset?
    assert ret == True          # the param is True, state is 'init', must return True


def test_sm4():
    '''Define a method of `StateMachine` called `process`. It must take a
       single parameter (referred to below as `sensed`), which can be True or False.
       The `process` method will be called over and over again, and must follow
       these rules:
       * If in the 'init' state, the function must return the value of the
         `sensed` parameter. If the `sensed` parameter is True, the state must
         be set to 'running'.
       * If in the 'running' state, the function must return 'True'. If
         the function has been called 20 times in the 'running' state, the 
         current state must be set to 'slowing'.
       * If in the 'slowing' state, the function must return 'True'. If
         the function has been called 10 times in the 'slowing' state, the
         current state must be set to 'init'.'''

    # run the state machine 10 times to see if it works
    sm = mycode.StateMachine('init')
    for cnt in range(10):
        for _ in run_the_test(sm, 'init'):
            pass

def test_sm5():
    '''This challenge is a more comprehensive test of the state machine'''

    for init_state in ['init', 'running', 'slowing']:
        sms = [mycode.StateMachine(init_state) for j in range(10)]
        gens = [run_the_test(sm, init_state) for sm in sms]

        dead = [False]*10

        while False in dead:
            for i, g in enumerate(gens):
                try:
                    if not dead[i]:
                        next(g)
                except StopIteration:
                    dead[i] = True

#
# Exceptions
#

# TODO

