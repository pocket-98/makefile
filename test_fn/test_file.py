#!/usr/bin/env python3

"""
 runs a program with specified input file and compare with stdout, stderr, & ret
 @file test_file.py
 @author Pavan Dayal
"""

import subprocess
import os
import sys

def get_prgm_output(prgm, inp=""):
    # run a program with or without input file
    if len(inp) == 0 or not os.path.exists(inp):
        cmd = prgm
    else:
        cmd = "%s < %s" % (prgm, inp)
    popen = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    popen.wait()

    # capture stdout, stderr, and return code
    out = popen.stdout.read().decode()
    err = popen.stderr.read().decode()
    ret = popen.returncode
    return ret, out, err

def partial_diff(expect, actual, n=5):
    # compare expected and actual strings and print 5 lines of diff
    exp = [e for e in expect.split("\n") if len(e) > 0]
    act = [a for a in actual.split("\n") if len(a) > 0]
    dif = list()
    ld = 0
    maxline = min(len(act), len(exp))
    for i in range(maxline):
        if act[i] != exp[i]:
            dif.append(i+1)
            ld += 1
        if ld >= n:
            break
    dexp = ("\n").join([exp[i-1] for i in dif])
    dact = ("\n").join([act[i-1] for i in dif])
    if ld < n:
        expmax = min(maxline+5-ld, len(exp))
        actmax = min(maxline+5-ld, len(act))
        if ld > 0:
            if expmax > maxline:
                dexp += "\n"
            if actmax > maxline:
                dact += "\n"
        dexp += ("\n").join(exp[maxline:expmax])
        dact += ("\n").join(act[maxline:actmax])
    return dif, dexp, dact

def check_prgm_output(cmd, inp="", exp="", experr="", expret=0, showErr=False):
    red = lambda x: "\033[0;31m" + str(x) + "\033[0m"
    green = lambda x: "\033[0;32m" + str(x) + "\033[0m"
    ret, out, err = get_prgm_output(cmd, inp)
    if len(exp) == 0 or not os.path.exists(exp):
        # check ret == 0 (and stderr = err)
        if len(experr) == 0 or not os.path.exists(experr):
            if ret == expret:
                print(green("passed"))
                if len(err) > 0 and showErr:
                    print("   stderr:", err.strip())
                return True
            else:
                print(red("failed"))
                print("   err code: %d" % ret)
                if err:
                    print("   stderr:", err.strip())
                return False
        else: # check stderr too
            experr_f = open(experr, "r")
            experr = experr_f.read()
            experr_f.close()
            if ret == expret and err == experr:
                print(green("passed"))
                if len(err) > 0 and showErr:
                    print("   stderr:", err.strip())
                return True
            else:
                print(red("failed"))
                print("   err code: %d" % ret)
                dif, dexp, dout = partial_diff(exp, out, 5)
                print("   error: %s vs %s stdout: lines %s" \
                    % (green("expected"), red("actual"), dif))
                print(green(dexp))
                print(red(dout))
                diferr, dexperr, derr = partial_diff(experr, err, 5)
                print("   error: %s vs %s stderr: lines %s" \
                    % (green("expected"), red("actual"), dif))
                print(green(dexperr))
                print(red(derr))
                return False
    else:
        # check ret == 0 and stdout == out (and stderr = err)
        exp_f = open(exp, "r")
        exp = exp_f.read()
        exp_f.close()
        if len(experr) == 0 or not os.path.exists(experr):
            if ret == expret and out == exp:
                print(green("passed"))
                if len(err) > 0 and showErr:
                    print("   stderr:", err.strip())
                return True
            else:
                print(red("failed"))
                print("   err code: %d" % ret)
                if err:
                    print("   stderr:", err.strip())
                dif, dexp, dout = partial_diff(exp, out, 5)
                print("   error: %s vs %s stdout: lines %s" \
                    % (green("expected"), red("actual"), dif))
                print(green(dexp))
                print(red(dout))
                return False
        else: # check stderr too
            experr_f = open(experr, "r")
            experr = experr_f.read()
            experr_f.close()
            if ret == expret and out == exp and err == experr:
                print(green("passed"))
                return True
            else:
                print(red("failed"))
                print("   err code: %d" % ret)
                dif, dexp, dout = partial_diff(exp, out, 5)
                print("   error: %s vs %s stdout: lines %s" \
                    % (green("expected"), red("actual"), dif))
                print(green(dexp))
                print(red(dout))
                diferr, dexperr, derr = partial_diff(experr, err, 5)
                print("   error: %s vs %s stderr: lines %s" \
                    % (green("expected"), red("actual"), dif))
                print(green(dexperr))
                print(red(derr))
                return False

if __name__ == "__main__":
    l = len(sys.argv)
    if l == 2:
        check_prgm_output(sys.argv[1]) # check(cmd)
    elif l == 3:
        check_prgm_output(sys.argv[1], "", sys.argv[2]) # check(cmd,"",out)
    elif l == 4:
        check_prgm_output(*(sys.argv[1:4])) # check(cmd, in, out)
    elif l == 5:
        check_prgm_output(*(sys.argv[1:5])) # check(cmd, in, out, ret)

