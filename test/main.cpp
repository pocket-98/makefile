/**
 * @file test/main.cpp
 * @author Pavan Dayal
 */

#include <cstdio>
#include <iostream>
#include <string>
#include "test_cpp.hpp"
#include "test_c.hpp"

std::string indent = " * ";

int main() {
    int fails = 0;
    int total = 0;
    int f, t;

    std::cerr << "testing cpp.hpp:" << std::endl;
    f = test_cpp::run_all();
    t = test_cpp::NUM_TESTS;
    fprintf(stderr, "passed (%d/%d): %.2f%%\n", t-f, t, 100.0*(t-f)/t);
    fails += f;
    total += t;

    std::cerr << "testing c.h:" << std::endl;
    f = test_c::run_all();
    t = test_c::NUM_TESTS;
    fprintf(stderr, "passed (%d/%d): %.2f%%\n", t-f, t, 100.0*(t-f)/t);
    fails += f;
    total += t;

    return f;
}
