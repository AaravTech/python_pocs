"""
Script to find subset which has max sum
Conditions -
    -   Calculate the sum of numbers that are non-adjacent
        elements with the maximum sum.
"""

import sys
import ast
import time
import decimal

__author__ = "Hardik Patel"
__version__ = "1.0"
__maintainer__ = "Hardik Patel"
__email__ = "hnmpatel@live.com"


class Calculator(object):
    def __init__(self, data):
        self.data = [int(n) for n in data]
        self.max_sum = None

    def find_max_sum_slower(self, data, possible_list):
        for i, m  in enumerate(data):
            if m < 0:
                continue
            possible_list.append(m)
            sum_of_possible_list = sum(possible_list)
            if self.max_sum is None:
                self.max_sum = sum_of_possible_list
            elif self.max_sum <= sum_of_possible_list:
                self.max_sum = sum_of_possible_list
            self.find_max_sum_slower(data[i+2:], possible_list)
            possible_list.pop()

    def find_max_sum_faster(self):
        first = 0
        second = 0
        temp = 0
        for e in self.data:
            temp = first if first > second else second
            if e < 0:
                second = first
            else:
                second = first + e
            first = temp

        self.max_sum = second if second > first else first

    def fine_subset_with_max_sum(self, faster=True):
        max_value = max(self.data)
        if max_value <= 0:
            self.max_sum = max_value
        else:
            if faster:
                self.find_max_sum_faster()
            else:
                self.find_max_sum_slower(self.data, [])
        return self.max_sum


if __name__ == "__main__":
    arguments = sys.argv[1:]
    if not len(arguments):
        print("Please enter numbers seperated by space or in list pattern.")
        exit()
    if len(arguments) == 1:
        data = ast.literal_eval(arguments[0])
    else:
        data = arguments
    if len(data) > 100:
        print("Please enter less then 100 numbers.")
        exit()

    # Calling first solution to find max sum of non-adjucent numbers.
    print("-"*80)
    print("Calling first solution...")
    print("-"*80)
    start_time = time.time()
    calc = Calculator(data)
    output = calc.fine_subset_with_max_sum(faster=False)
    end_time = time.time()
    print("Answer: ", output)
    print("Time:  %.7f " % float(end_time - start_time), "\n")

    # Calling Second solution to find max sum of non-adjucent numbers.
    print("-"*80)
    print("Calling second solution...")
    print("-"*80)
    start_time = time.time()
    calc = Calculator(data)
    output = calc.fine_subset_with_max_sum()
    end_time = time.time()
    print("Answer: ", output)
    print("Time:  %.7f " % float(end_time - start_time), "\n")
