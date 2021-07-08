import re
import sys
import math

from operator import itemgetter, attrgetter

class L3Programs:
    def __init__(self):
        pass

    def program_18(self):
        ''' 
        A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
        Following are the criteria for checking the password:
        1. At least 1 letter between [a-z]
        2. At least 1 number between [0-9]
        1. At least 1 letter between [A-Z]
        3. At least 1 character from [$#@]
        4. Minimum length of transaction password: 6
        5. Maximum length of transaction password: 12
        Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.
        Example
        If the following passwords are given as input to the program:
        ABd1234@1,a F1#,2w3E*,2We3345
        Then, the output of the program should be:
        ABd1234@1

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input. 
        '''
        p1 = re.compile("[a-z]")
        p2 = re.compile("[A-Z]")
        p3 = re.compile("[0-9]")
        p4 = re.compile("[$#@]")
        result = []
        passwords = raw_input().split(',')
        for password in passwords:            
            if len(password) > 12 or len(password) <6 or not p1.search(password) or not p2.search(password) or not p3.search(password) or not p4.search(password) :
                continue
            result.append(password)
        print(",".join(result))

    def program_19(self):
        ''' You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
        1: Sort based on name;
        2: Then sort based on age;
        3: Then sort by score.
        The priority is that name > age > score.
        If the following tuples are given as input to the program:
        Tom,19,80
        John,20,90
        Jony,17,91
        Jony,17,93
        Json,21,85
        Then, the output of the program should be:
        [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input.
        We use itemgetter to enable multiple sort keys. '''

        people = []
        while True:
            s = raw_input()
            if s:
                people.append(tuple(s.split(',')))
            else:
                break
        people = sorted(people, key=itemgetter(0,1,2))
        print(people)

    def program_20(self):
        ''' Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

        Hints:
        Consider use yield '''

        def c_generator(n):
            for i in range(n):
                if i%7 == 0:
                    yield i

        n = raw_input()
        print([i for i in c_generator(int(n))])

    def program_21(self):
        ''' A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
        UP 5
        DOWN 3
        LEFT 3
        RIGHT 2
        
        The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.
        Example:
        If the following tuples are given as input to the program:
        UP 5
        DOWN 3
        LEFT 3
        RIGHT 2
        Then, the output of the program should be:
        2

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input. '''

        commands = []
        start = (0, 0)
        end = (0, 0)
        while True:
            s = raw_input()
            if s:
                commands.append(tuple(s.split()))
            else:
                break
        for operation, value in commands:
            if operation == "UP":
                end = (end[0], end[1] + int(value))
            elif operation == "DOWN":
                end = (end[0], end[1] - int(value))
            elif operation == "LEFT":
                end = (end[0] - int(value), end[1])
            else:
                end = (end[0] + int(value), end[1])

        distance = int(round(math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)))
        print(distance)

    def program_22(self):
        ''' Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically. 
        Suppose the following input is supplied to the program:
        New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
        Then, the output should be:
        2:2
        3.:1
        3?:1
        New:1
        Python:5
        Read:1
        and:1
        between:1
        choosing:1
        or:2
        to:1

        Hints
        In case of input data being supplied to the question, it should be assumed to be a console input. '''

        sentence = raw_input()
        words = sentence.split()
        result = {}
        for word in words:
            if word in result.keys():
                result[word]+=1
            else:
                result[word] = 1
        for word in sorted(result.keys()):
            print(word+":"+str(result[word]))

    def program_23(self):
        pass
 


import sys
n = sys.argv[1]
l3 = L3Programs()
getattr(l3, 'program_%s' % n)()