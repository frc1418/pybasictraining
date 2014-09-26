#!/bin/bash

MAXTESTS=5

if [ "$1" == "" ]; then
    echo "Usage: ./run_single.sh TEST_NUMBER"
    exit 1
fi

if ! test "$1" -gt 0 2> /dev/null ; then
    echo "ERROR: Specified test must be a number greater than zero (is '$1')"
    exit 1
fi

if ! test "$1" -lt $MAXTESTS 2> /dev/null ; then
    echo "ERROR: Specified test must be a number less than $MAXTESTS (is '$1')"
    exit 2
fi


TESTNAME=test_challenges.py::test_$1
shift

cd `dirname $0`/tests/
PYTHONPATH="../src" python3 -m pytest $@ $TESTNAME
