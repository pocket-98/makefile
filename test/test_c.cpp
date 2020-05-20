/**
 * @file test/test_c.cpp
 * @author Pavan Dayal
 */

#include "test_c.hpp"
#include <sstream>
#include <cstring>

int test_c::test_concat() {
    int argc;
    char* argv[3];
    char argv0[256], argv1[256], argv2[256];
    char out[256];
    int len;

    argc = 1;
    sprintf(argv0, "./a.out");
    argv[0] = argv0;
    len = concatStrs(argc, argv, out);
    testequal("num chars incorrect", 0, len);
    testequal("0 args incorrect", std::string(""), std::string(out))

    argc = 2;
    sprintf(argv1, "1");
    argv[1] = argv1;
    len = concatStrs(argc, argv, out);
    testequal("num chars incorrect", 3, len);
    testequal("1 arg incorrect", std::string("[1]"), std::string(out))

    argc = 3;
    sprintf(argv2, "2");
    argv[2] = argv2;
    len = concatStrs(argc, argv, out);
    testequal("num chars incorrect", 7, len);
    testequal("2 args incorrect", std::string("[1] [2]"), std::string(out))

    return EXIT_SUCCESS;
}

int test_c::run_all() {
    int fails = 0;
    testfn(fails, test_c::test_concat, "concatStr()");
    return fails;
}
