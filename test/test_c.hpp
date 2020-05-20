/**
 * test c.c
 * @file test_c.hpp
 * @author Pavan Dayal
 */
#ifndef TEST_C_HPP
#define TEST_C_HPP

#include "test.hpp"
#include "../cpp.hpp"

namespace test_c {
    // return 0 for success and 1 for failure
    int test_concat();

    // returns number of failures for all tests
    const int NUM_TESTS = 1;
    int run_all();
}

#endif // TEST_C_HPP
