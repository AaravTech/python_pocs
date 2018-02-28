class L2Programs:
    def __init__(self):
        pass

    def program_8(self):
        ''' 
        Question 8
        ==========
        Question:
        Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
        Suppose the following input is supplied to the program:
        without,hello,bag,world
        Then, the output should be:
        bag,hello,without,world

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input. '''

        input_str = raw_input()
        l = [i.strip() for i in input_str.split(',')]
        d = sorted(l)
        print(','.join(d)) 
       
    def program_9(self):
        ''' 
        ====================================================================
        Question 9
        Level 2

        Question:
        Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
        Suppose the following input is supplied to the program:
        Hello world
        Practice makes perfect
        Then, the output should be:
        HELLO WORLD
        PRACTICE MAKES PERFECT

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input.
        '''

        l = []
        while True:
            s = raw_input()
            if s:
                l.append(s)
            else:
                break
        for s in l:
            print(s.upper())

    def program_10(self):
        ''' Question 10
        Level 2

        Question:
        Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
        Suppose the following input is supplied to the program:
        hello world and practice makes perfect and hello world again
        Then, the output should be:
        again and hello makes perfect practice world

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input.
        We use set container to remove duplicated data automatically and then use sorted() to sort the data. '''

        sentence = raw_input()
        answer = " ".join(sorted(list(set(sentence.split()))))
        print(answer)

    def program_11(self):
        ''' Question 11
        Level 2

        Question:
        Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
        Example:
        0100,0011,1010,10010100,0011,1010,1001
        Then the output should be:
        1010
        Notes: Assume the data is input by console.

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input. '''

        data = raw_input()
        b_numbers = data.split(',')
        print(",".join([b for b in b_numbers if int(b,2)%5==0]))

    def program_12(self):
        ''' 
        Question 12
        Level 2

        Question:
        Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
        The numbers obtained should be printed in a comma-separated sequence on a single line.

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input.
        '''
        r = []
        for n in range(1000, 3001):
            f = False
            for c in str(n):
                if int(c)%2 == 0:
                    f = True
                else:
                    f = False
                    break
            if f:
                r.append(str(n))
        print(",".join(r))

    def program_13(self):
        '''
        Write a program that accepts a sentence and calculate the number of letters and digits.
        Suppose the following input is supplied to the program:
        hello world! 123
        Then, the output should be:
        LETTERS 10
        DIGITS 3

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input.
        '''
        digits = 0
        letters = 0
        sentence = raw_input()
        for c in sentence:
            if c.isdigit():
                digits += 1
            elif c.isalpha():
                letters += 1
        print("LETTERS " + str(letters))
        print("DIGITS " + str(digits))

    def program_14(self):
        ''' 
        Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
        Suppose the following input is supplied to the program:
        Hello world!
        Then, the output should be:
        UPPER CASE 1
        LOWER CASE 9

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input. 
        '''
        upper = 0
        lower = 0
        sentence = raw_input()
        for c in sentence:
            if c.isupper():
                upper += 1
            elif c.islower():
                lower += 1
        print("UPPER CASE " + str(upper))
        print("LOWER CASE " + str(lower))
        
    def program_15(self):
        ''' 
        Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
        Suppose the following input is supplied to the program:
        9
        Then, the output should be:
        11106

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input.
        '''

        n = raw_input()
        result = 0
        for i in range(1, 5):
            result += int(n*i)
        print(result)

    def program_16(self):
        ''' 
        Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
        Suppose the following input is supplied to the program:
        1,2,3,4,5,6,7,8,9
        Then, the output should be:
        1,3,5,7,9

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input.
        '''

        numbers = raw_input().split(",")
        squared = [n for n in numbers if int(n)%2!=0]
        print(",".join(squared))

    def program_17(self):
        '''
        Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:
        D 100
        W 200
        
        D means deposit while W means withdrawal.
        Suppose the following input is supplied to the program:
        D 300
        D 300
        W 200
        D 100
        Then, the output should be:
        500

        Hints:
        In case of input data being supplied to the question, it should be assumed to be a console input.
        '''

        amount = 0
        transactions = []
        while True:
            data = raw_input()
            if data:
                transactions.append(tuple(data.split()))
            else:
                break
        for operation, value in transactions:
            if operation == "D":
                amount += int(value)
            else:
                amount -= int(value)
        print(amount)


import sys
n = sys.argv[1]
l2 = L2Programs()
getattr(l2, 'program_%s' % n)()