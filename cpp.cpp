/**
 * link c function with cpp
 * @file cpp.cpp
 * @author Pavan Dayal
 */

#include <iostream>
#include "cpp.hpp"

int main(int argc, char* argv[]) {
    char out[256];
    std::cout << "args: ";

    concatStrs(argc, argv, out);

    cpp::coutChars(out);
    std::cout << std::endl << cpp::times2(4) << std::endl;
	return 0;
}

void cpp::coutChars(const char* str) {
    std::cout << std::string(str);
}

int cpp::times2(int n) {
    return 2*n;
}
