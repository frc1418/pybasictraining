@echo off

setlocal

if "%1" == "" echo Usage: run_single.bat TEST_NUMBER
if "%1" == "" goto end

cd %~dp0\tests
set PYTHONPATH=..\src
set TESTNAME=test_challenges.py::test_%1

for /f "tokens=1,* delims= " %%a in ("%*") do set ALL_BUT_FIRST=%%b

py -3 -m pytest -l %ALL_BUT_FIRST% %TESTNAME%

:end

endlocal
