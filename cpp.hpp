/*
 * get extern to C function
 * @file cpp.hpp
 * @author Pavan Dayal
 */

#ifndef CPP_HPP
#define CPP_HPP

// c fn to concat array of n strings to the out string
extern "C" int concatStrs(int n, char* strs[], char* out);

namespace cpp {
    void coutChars(const char* str);
    int times2(int n);
}

#endif // CPP_HPP
