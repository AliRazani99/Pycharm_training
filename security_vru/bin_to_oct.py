import numpy as np


class Security:

    def __init__(self, number):
        self.number = number

    def split_number_s0(self):
        digits = [int(x) for x in str(self.number)]
        print(digits)
        s0 = []
        for i in range(len(digits)):
            print([self.s0(digits[i])])
            s0 += [self.s0(digits[i])]
        return s0

    def split_number_s1(self,p0):
        digits = [int(x) for x in str(p0)]
        print(digits)
        s1 = []
        for i in range(len(digits)):
            print([self.s1(digits[i])])
            s1 += [self.s1(digits[i])]
        print("s1 :",s1)
        return s1

    def split_number_p0(self):
        digits = [int(x) for x in str(self.number)]
        print(digits)
        p0 = []
        for i in range(len(digits)):
            print([self.p0(digits[i])])
            p0 += [self.p0(digits[i])]
        self.split_number_s1(p0)
        return p0

    def split_number_p1(self):
        digits = [int(x) for x in str(self.number)]
        print(digits)
        p1 = []
        for i in range(len(digits)):
            print([self.p1(digits[i])])
            p1 += [self.p1(digits[i])]
        return p1

    def s0(self, binary_key):

        if binary_key == 0:
            return 1
        elif binary_key == 1:
            return 3
        elif binary_key == 2:
            return 5
        elif binary_key == 3:
            return 2
        elif binary_key == 4:
            return 6
        elif binary_key == 5:
            return 6
        elif binary_key == 6:
            return 7
        elif binary_key == 7:
            return 0

    def s1(self, binary_key):

        if binary_key == 0:
            return 5
        elif binary_key == 1:
            return 3
        elif binary_key == 2:
            return 7
        elif binary_key == 3:
            return 4
        elif binary_key == 4:
            return 6
        elif binary_key == 5:
            return 2
        elif binary_key == 6:
            return 0
        elif binary_key == 7:
            return 1

    def p0(self, binary_key):

        if binary_key == 0:
            return 5
        elif binary_key == 1:
            return 6
        elif binary_key == 2:
            return 4
        elif binary_key == 3:
            return 2
        elif binary_key == 4:
            return 7
        elif binary_key == 5:
            return 0
        elif binary_key == 6:
            return 3
        elif binary_key == 7:
            return 1

    def p1(self, binary_key):

        if binary_key == 0:
            return 4
        elif binary_key == 1:
            return 6
        elif binary_key == 2:
            return 7
        elif binary_key == 3:
            return 1
        elif binary_key == 4:
            return 3
        elif binary_key == 5:
            return 2
        elif binary_key == 6:
            return 5
        elif binary_key == 7:
            return 0


if __name__ == '__main__':
    s1 = []
    binary_key = 13471
    number = Security(binary_key)
    p0 = number.split_number_p0()
    print("p0 is :",p0)



