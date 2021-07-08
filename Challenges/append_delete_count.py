"""
Script to find given operation count is corret to achieve from 
one string to other string by doing append and remove last character
"""

import sys
import time
import decimal

__author__ = "Hardik Patel"
__version__ = "1.0"
__maintainer__ = "Hardik Patel"
__email__ = "hnmpatel@live.com"


class StringManipulation(object):
    def __init__(self, from_s, to_s):
        self.from_s = from_s
        self.l1 = len(self.from_s)
        self.to_s = to_s
        self.l2 = len(self.to_s)
        self.total = self.l1 + self.l2

    def find_common_string_length(self):
        first = self.from_s
        second = self.to_s
        if self.l1 > self.l2:
            first = self.to_s
            second = self.from_s
        ret = 0
        for i, c in enumerate(first):
            if c == second[i]:
                ret += 1
                continue
            else:
                break
        return ret

    def is_even(self, n):
        print(n)
        print(n % 2)
        return n % 2 == 0

    def assert_operation_count(self, n):
        l = self.find_common_string_length()
        e = self.l1 + self.l2 - 2*l
        print("total =", self.total, "  n =", n,"  l =", l, "  e =", e)
        if n == e:
            print("same")
            return True
        else:
            if n > e:
                if self.is_even(n-e):
                    return True
                else:
                    if n > self.total:
                        return True
            else:
                return False
        return False
        

HELP = """
Please provide arguments in following fashion
    <scriptname> "from string" "To string" "number to assert"
"""

def exit_with_help(msg=None):
    if(msg):
        print(msg)
    print(HELP)
    exit()

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) != 3:
        exit_with_help()
    try:
        from_s = arguments[0].lower()
        to_s = arguments[1].lower()
        if len(from_s) > 100 or len(to_s) > 100:
            exit_with_help("Length of provided string must be less than 100.")
        n = int(arguments[2])
        if n > 100:
            exit_with_help("please provde number between 0 and 100.")
    except Exception as e:
        exit_with_help("Provided arguments are not valid!")

    # Calling first solution to find max sum of non-adjucent numbers.
    print("-"*80)
    print("Calling first solution...")
    print("-"*80)
    start_time = time.time()
    sm = StringManipulation(from_s, to_s)
    output = sm.assert_operation_count(n)
    end_time = time.time()
    print("Answer: ", output)
    print("Time:  %.7f " % float(end_time - start_time), "\n")
