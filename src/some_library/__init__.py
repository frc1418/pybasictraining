#
# To legally & successfully complete the challenges, you MUST NOT change the 
# contents of this file!
#

_retval = {
    'teapot': True
}

_called = {
    'teapot': False,
    'multiply': False
}

def i_am_a_teapot():
    print("I AM A TEAPOT!")
    _called['teapot'] = True

    return _retval['teapot']


def multiply_by_2(parameter):
    _called['multiply'] = True
    return parameter * 3 # ha


