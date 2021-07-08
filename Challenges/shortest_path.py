"""
Script to find given operation count is corret to achieve from 
one string to other string by doing append and remove last character
"""

import sys
import time
import ast
import decimal

from operator import itemgetter

__author__ = "Hardik Patel"
__version__ = "1.0"
__maintainer__ = "Hardik Patel"
__email__ = "hnmpatel@live.com"


class Path:
    path = []
    distance = 0

    def __str__(self):
        return "{0} - {1}".format(self.path, self.distance)

class PathManipulation(object):
    def __init__(self, all_paths=[]):
        self.all_paths = all_paths
        self.dist = 0
        self.source = None
        self.destination = None
        self.final_path = Path()
        self.possible_paths = []

    def find_possible_paths(self, remaining_paths, source):
        filtered_paths = [p for p in remaining_paths if p[0]==source]
        print(filtered_paths)
        remaining_paths = [x for x in self.all_paths if x not in filtered_paths]
        p_paths = []
        for p in filtered_paths:
            new_source = p[1]
            returned_paths = self.find_possible_paths(paths, new_source)
            print(returned_paths)
            path = Path()
            path.path.append(new_source)
            path.distance = p[2]
            p_paths.append(path)
        return p_paths


    def find_shortest_path(self, path):
        self.source = path[0]
        self.destination = path[1]
        can_be_reached = any([p[1]==self.destination for p in self.all_paths])
        can_be_started = any([p[0]==self.source for p in self.all_paths])
        if not (can_be_reached and can_be_started):
            return False

        result = self.find_possible_paths(self.all_paths, self.source)
        print(result)


        

HELP = """
Please provide arguments in following fashion
    python <scriptname> "[[source, destination, distance], ]" "[source, destinationn]"

Example - 
    python shortest_path "[['A', 'B', 2], ['B', 'C', 2], ['A', 'C', 3]]" "['A', C']"
"""

def exit_with_help(msg=None):
    if(msg):
        print(msg)
    print(HELP)
    exit()

if __name__ == "__main__":
    arguments = sys.argv[1:]
    if len(arguments) != 2:
        exit_with_help()
    try:
        all_paths = ast.literal_eval(arguments[0])
        path = ast.literal_eval(arguments[1])
        if not (isinstance(all_paths, list) or isinstance(path, list)):
            raise Exception()
    except Exception as e:
        exit_with_help("Provided arguments are not valid!")

    # Calling first solution to find max sum of non-adjucent numbers.
    print("-"*80)
    print("Calling first solution...")
    print("-"*80)
    start_time = time.time()
    p = PathManipulation(all_paths)
    output = p.find_shortest_path(path)
    end_time = time.time()
    print("Answer: ", output)
    print("Time:  %.7f " % float(end_time - start_time), "\n")
