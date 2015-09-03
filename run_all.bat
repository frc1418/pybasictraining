@echo off

setlocal

cd %~dp0\tests
set PYTHONPATH="..\src"
py -3 -m pytest -l --color=no %*

endlocal
