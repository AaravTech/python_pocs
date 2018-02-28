class L3Programs:
    def __init__(self):
        pass

    def program_18(self):
        pass

    def program_19(self):
        pass

    def program_20(self):
        pass

    def program_21(self):
        pass

    def program_22(self):
        pass

    def program_23(self):
        pass
 


import sys
n = sys.argv[1]
l3 = L3Programs()
getattr(l3, 'program_%s' % n)()