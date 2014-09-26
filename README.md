pybasictraining
===============

This is a repository that we'll use as a tool to teach you python. This is an
interactive learning experiment that gives you a number of challenges to
beat, and you need to write python code that will allow the tests to succeed.

Starting out
============

You need to have the following things installed:

* [Python 3](https://www.python.org/downloads/release/python-341/)
* py.test (If you have [pip installed](http://pip.readthedocs.org/en/latest/installing.html),
  you can `pip install pytest`)
  
Currently this is geared towards running the tests on Linux/OSX. At some
point I might add Windows support too.

Get the code
------------

First, you need to clone this repository somewhere. You can use eclipse to
do this, or open up a terminal and run the following:

	git clone https://github.com/frc1418/pybasictraining.git

Testing to see if you beat the challenges
-----------------------------------------

The challenges currently need to be ran from the terminal. This means you
need to open up a terminal, and change directories to wherever you checked
out the code. For help using the terminal, see [this resource](http://team1418.org/wiki/CommandLinePrimer).

There are two ways to run the challenges. If you think your code can beat ALL
of the challenges, then you can do the following:

	./run_all.sh

However, running all the challenges can be a bit confusing and give you a lot
of errors that you don't care about when concentrating on beating the current
challenge. To run a single challenge, do this instead:

	./run_single.sh CHALLENGE_NUMBER
	
So for example, to run challenge #3, you would do this:

	./run_single.sh 3


Should be simple enough!

The challenges
==============

Variables
---------

1. Create a file called `mycode.py` in the `src` directory
2. Define a variable named `x`, and make it equal to the number `3`

Functions
---------

3. Define a function called `do_something`
4. `do_something` should take two parameters, `x1` and `x2`
5. `do_something` should have a docstring that says "This does something"
6. `do_something` should return the result of `x1` times `x2`

7. Define a function called `return_things`

Modules
-------
   
Objects
-------



   
If you're having problems
=========================

1. Google for the solution (or bing, whatever)
2. Send an email to your peers, and see if they can help
3. Send an email to your team's mentor(s)

Most of the things that we're doing here is pretty simple, and google should
be able to point you to answers. Often, it will point you at [Stack Overflow](http://stackoverflow.com),
which is a really excellent resource for lots of programming questions.



