pybasictraining
===============

This is a repository that we'll use as a tool to teach you python. This is an
interactive learning experiment that gives you a number of challenges to
beat. To pass the challenges you will need to write python code.

Once you have passed these challenges, and understand the concepts required
for passing the challenges, you should have a reasonable grasp of how to do
a lot of basic things in python.

Preparation
===========

You need to have the following things installed:

* [Python 3](https://www.python.org/downloads/release/python-341/)
* py.test (If you have [pip installed](http://pip.readthedocs.org/en/latest/installing.html),
  you can `pip install pytest`)
  
Currently this is geared towards running the tests on Linux/OSX. At some
point I might add Windows support too.

Get the code
------------

You need to clone this git repository somewhere on your computer. You can use
eclipse to do this, or open up a terminal and run the following:

	git clone https://github.com/frc1418/pybasictraining.git

About the challenges
--------------------

In [the challenges](#the-challenges) section, each bullet point is a challenge you must complete.
The name of the challenge is listed first, followed by the description of
the challenge.

Please keep in mind that there are generally many different ways you can get
the challenge tests to pass, but typically each test is a simple step that
builds upon the knowledge/things done in previous tests. You are encouraged
to complete the tests in order.


Testing to see if you beat the challenges
-----------------------------------------

The challenges currently need to be run in the terminal. This means you
need to open up a terminal and change directories to wherever you checked
out the code. For help using the terminal, see [this resource](http://team1418.org/wiki/CommandLinePrimer).

There are two ways to run the challenges. If you think your code can beat ALL
of the challenges, then you can do the following:

	./run_all.sh

However, running all the challenges can be a bit confusing and give you a lot
of errors that you don't care about when concentrating on beating the current
challenge. To run a single challenge, do this instead:

	./run_single.sh CHALLENGE
	
So for example, to run challenge `v1`, you would do this:

	./run_single.sh v1


Should be simple enough!

The Challenges
==============

Creating files
--------------

* s1 - Create a file called `mycode.py` in the `src` directory

Variables
---------

The code for these challenges should be added to `mycode.py`

* v1 - Define a variable named `x`, and make it equal to the number `3`
* v2 - Define a variable named `s`, and make it a string that says `I am a string`
* v3 - Define a variable named `b`, and make it equal to the boolean false value

Functions & logic
-----------------

The code for these challenges should be added to `mycode.py`

* f1 - Define a function called `do_something`
* f2 - `do_something` should take two parameters, `x1` and `x2`
* f3 - `do_something` should have a docstring that says "This does something"
* f4 - `do_something` should return the result of `x1` times `x2`

* f5 - Define a function called `keyword_fn`, it should take a keyword argument
  called `keyword`, with a default value of `None`
* f6 - If `keyword` is None, then `keyword_fn` should return the string 'No'.
  Otherwise, it should return the keyword argument plus `2`

* f7 - Define a function called `return_many`, it should take three parameters
* f8 - `return_many` should add '2' to each of the parameters, and return the
  three parameters as a tuple
* f9 - Call `return_many` with the parameters 1, 2, and 3, and assign the
  returned values to the variables r1, r2, and r3

Modules
-------

The code for these challenges should be added to `mycode.py`

* m1 - Import the library called `some_library`
* m2 - Call the `i_am_a_teapot` function inside of `some_library`, store its
  return value in a variable called `teapot`
* m3 - Define a function called `gonna_call_stuff`, and have it take a
  single parameter
* m4 - From the `gonna_call_stuff` function, call the `multiply_by_2` function
  in the `some_library` library with the first parameter equal to the first
  parameter of the `gonna_call_stuff` function, and return the value returned by
  `multiply_by_2`

Tuples
------

The code for these challenges should be added to `mycode.py`

* t1 - Define a variable `t1`, and make it equal to an empty tuple
* t2 - Define a variable `t2`, and make it equal to a tuple containing the value False
* t3 - Define a variable `t3`, and make it equal to a tuple containing 32000 elements
* t4 - Define a variable `t4`, and make it equal to a tuple containing the values
  'foo', 1, and False in it (in that order).
* t5 - Define a variable `t5`, and make it equal to the 0th element of `t4`

* t6 - Define a function called `measure_tuple`, that takes a single parameter
* t7 - `measure_tuple` should return the number of elements present in the
  tuple
  
* t8 - Define a function called `sum_tuple`, that takes a single parameter
* t9 - In `sum_tuple`, the parameter is a tuple. If there are 5 elements in
  the tuple, return the sum of the elements in the tuple. Otherwise, return None.

Lists
-----

The code for these challenges should be added to `mycode.py`

* l1 - Define a variable `l1`, and make it equal to an empty list
* l2 - Define a variable `l2`, and make it equal to a list containing the value False
* l3 - Define a variable `l3`, and make it equal to a list containing 32000 elements
* l4 - Define a variable `l4`, and make it equal to a list containing the values
  'foo', 1, and False in it (in that order).
* l5 - Define a variable `l5`, and make it equal to the 0th element of `l4`

* l6 - Define a function called `measure_list`, that takes a single parameter
* l7 - `measure_list` should return the number of elements present in the
  list
  
* l8 - Define a function called `sum_list`, that takes a single parameter
* l9 - In `sum_list`, the parameter is a list. If there are 5 elements in
  the list, return the sum of the elements in the list. Otherwise, return None.

* l10 - Define a function called `wopit` that takes a single parameter, and
  returns None. The parameter is a list. Add the first element of the list to the
  end of the list. Do nothing if the list is empty.
* l11 - Define a function called `bopit` that takes a single parameter, and
  returns None. The parameter is a list. Remove an item from the end of the list.
  Do nothing if the list is empty.
* l12 - Define a function called `mopit` that takes a single parameter, and
  returns None. The parameter is a list. Remove an item from the beginning of the list.
  Do nothing if the list is empty.

* l13 - Define a function called `zopit` that takes a single parameter. The
  parameter is a list. Return True if there is an element in the list that is
  equal to the string `item`, and the element position in the list is greater
  than 100.


Dictionaries
------------

TODO

Classes & objects
-----------------

TODO


Exceptions
----------

TODO

   
If you're having problems
=========================

1. Google for the solution (or bing, whatever)
2. Send an email to your peers, and see if they can help
3. Send an email to your team's mentor(s)

Most of the things that we're doing here is pretty simple, and google should
be able to point you to answers. Often, it will point you at [Stack Overflow](http://stackoverflow.com),
which is a really excellent resource for lots of programming questions.



