/**
 * @file test/test_cpp.cpp
 * @author Pavan Dayal
 */

#include "test_cpp.hpp"
#include <sstream>
#include <cstring>

int test_cpp::test_cout() {
    const char* str = "thing";
    cpp::coutChars(str);
    //testequal("incorrect print", std::string("thing"), std::string(str))
    return EXIT_SUCCESS;
}

int test_cpp::test_double() {
    testequal("didn't double num", 2, cpp::times2(1))
    testequal("didn't double negative num", -4, cpp::times2(-1-1))
    return EXIT_SUCCESS;
}

int test_cpp::run_all() {
    int fails = 0;
    testfn(fails, test_cpp::test_cout, "cpp::test_cout()");
    testfn(fails, test_cpp::test_double, "cpp::test_double()");
    return fails;
}

void cpp::coutChars(const char* str) {
    std::cout << std::string(str);
}

int cpp::times2(int n) {
    return 2*n;
}
