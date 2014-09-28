#!/bin/bash

cd `dirname $0`/tests/
PYTHONPATH="../src" python3 -m pytest -l $@
