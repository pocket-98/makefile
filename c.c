/**
 * concat strings
 * @file c.c
 * @author Pavan Dayal
 */
#include <stdio.h>
#include <stdbool.h>
#include "c.h"

int concatStrs(int n, char* strs[], char* out) {
    int j, diff;
    int k = 0;
    bool ranOnce = false;

    for (j=1; j<n; ++j) {
        // append a space if not first str
        if (ranOnce) {
            *(out++) = ' ';
            ++k;
        } else {
            ranOnce = true;
        }

        // append next str
        diff = sprintf(out, "[%s]", strs[j]);
        out += diff;
        k += diff;
    }

    // end str
    *out = '\0';
    return k;
}
