/**
 * test cpp.cpp
 * @file test_cpp.hpp
 * @author Pavan Dayal
 */
#ifndef TEST_CPP_HPP
#define TEST_CPP_HPP

#include "test.hpp"
#include "../cpp.hpp"

namespace test_cpp {
    // return 0 for success and 1 for failure
    int test_cout();
    int test_double();

    // returns number of failures for all tests
    const int NUM_TESTS = 2;
    int run_all();
}

#endif // TEST_CPP_HPP

