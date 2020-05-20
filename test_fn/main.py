#!/usr/bin/env python3

"""
 run a.out with given command line args/input and compare to stdout and stderr
 @file main.py
 @author Pavan Dayal
"""

import os
import sys
import re
import subprocess
from test_file import check_prgm_output as check

###########
# <SETUP> #
###########
test_folder = "./test_fn/"
exe = ("./a.out" if len(sys.argv) == 1 else sys.argv[1])

use_valgrind = False
if use_valgrind:
    exe = "valgrind -v --track-fds=yes --leak-check=full " + exe
###########
# </SETUP> #
###########

files = set(os.listdir(test_folder))
files -= {f for f in files if ".py" in f}

ins = {f for f in files if "in" in f}
files -= ins

args = {f for f in files if "arg" in f}
files -= args

outs = {f for f in files if "exp" in f or "out" in f}
files -= outs

errs = {f for f in files if "err" in f}
files -= errs

rets = {f for f in files if "ret" in f}

ins = list(ins)
ins.sort()

getn = re.compile("[0-9]+")
nums = list()
for i in ins:
    n = getn.search(i)
    if n:
        nums += [n.group(0)]

passed = 0
total = len(nums)
i = 1
for num in nums:
    arg = [f for f in args if num in f]
    arg = "" if len(arg) != 1 else test_folder+arg[0]
    inp = [f for f in ins if num in f]
    inp = "" if len(inp) != 1 else test_folder+inp[0]
    out = [f for f in outs if num in f]
    out = "" if len(out) != 1 else test_folder+out[0]
    err = [f for f in errs if num in f]
    err = "" if len(err) != 1 else test_folder+err[0]
    ret = [f for f in rets if num in f]
    ret = "" if len(ret) != 1 else test_folder+ret[0]
    cmd = exe
    cmd_print = cmd
    if arg:
        subprocess.Popen("envsubst < %s > tmparg" % arg, shell=True)
        cmd += " $(cat tmparg)"
        cmd_print += " $(cat %s)" % arg
    if inp:
        subprocess.Popen("envsubst < %s > tmpinp" % inp, shell=True)
        cmd += " < tmpinp"
        cmd_print += " < %s" % inp
    if out:
        subprocess.Popen("envsubst < %s > tmpout" % out, shell=True)
        out = "tmpout"
    if err:
        subprocess.Popen("envsubst < %s > tmperr" % err, shell=True)
        err = "tmperr"
    if ret:
        f = open(ret)
        ret = int(f.read())
        f.close()
    else:
        ret = 0

    print(" * test %2d: %-60s" % (i, cmd_print), end="", flush=True)
    if check(cmd, "", out, err, ret, showErr=True):
        passed += 1
    i += 1

try:
    percent = 100.0 * passed / total
    os.remove("tmparg")
    os.remove("tmpinp")
    os.remove("tmpout")
    os.remove("tmperr")
except:
    percent = 100.0

print("passed (%d/%d): %.2f%%" % (passed, total, percent))
