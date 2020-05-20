# makefile
Starter Template C and C++ with Unit Testing, Functional Testing, and Line Coverage

usage:
 * `make`: build a.out
 * `make test`: build a.out-test using test/main.cpp
 * `make cov`: recompile with -fprofile-arcs a.out-cov using test/main.cpp

other useful things:
 * `test/test.hpp` macros for asserting if vars are equal
 * `test_fn/test_file.py` which runs a command and gets stdout/stderr/retcode
 * `test_fn/main.py` pretty print exp/actual diff with colors for each test
