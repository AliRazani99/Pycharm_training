import numpy as np
class Security:

    def __init__(self):
        self.one = 1
        self.two = 3
        self.three = 4
        self.four = 7
        self.five = 1

    # def split_number_s0(self):
    #     digits = [int(x) for x in str(self.number)]
    #     print(digits)
    #     s0 = []
    #     for i in range(len(digits)):
    #         print([self.s0(digits[i])])
    #         s0 += [self.s0(digits[i])]
    #     return s0
    #
    # def split_number_s1(self,p0):
    #     digits = [int(x) for x in str(p0)]
    #     print(digits)
    #     s1 = []
    #     for i in range(len(digits)):
    #         print([self.s1(digits[i])])
    #         s1 += [self.s1(digits[i])]
    #     print("s1 :",s1)
    #     return s1
    #
    # def split_number_p0(self):
    #     digits = [int(x) for x in str(self.number)]
    #     print(digits)
    #     p0 = []
    #     for i in range(len(digits)):
    #         print([self.p0(digits[i])])
    #         p0 += [self.p0(digits[i])]
    #     self.split_number_s1(p0)
    #     return p0

    #
    # def split_number_p1(self):
    #     digits = [int(x) for x in str(self.number)]
    #     print(digits)
    #     p1 = []
    #     for i in range(len(digits)):
    #         print([self.p1(digits[i])])
    #         p1 += [self.p1(digits[i])]
    #     return p1
    def run(self):
        print("input is: ", self.one, self.two, self.three, self.four, self.five)
        p0_1 = self.p0(self.one)
        p0_2 = self.p0(self.two)
        p0_3 = self.p0(self.three)
        p0_4 = self.p0(self.four)
        p0_5 = self.p0(self.five)
        print(p0_1, p0_2, p0_3, p0_4, p0_5)
        s1_1 = self.s1(p0_1)
        s1_2 = self.s1(p0_2)
        s1_3 = self.s1(p0_3)
        s1_4 = self.s1(p0_4)
        s1_5 = self.s1(p0_5)
        print(s1_1, s1_2, s1_3, s1_4, s1_5)
        p1_1 = self.p1(s1_1)
        p1_2 = self.p1(s1_2)
        p1_3 = self.p1(s1_3)
        p1_4 = self.p1(s1_4)
        p1_5 = self.p1(s1_5)
        print(p1_1, p1_2, p1_3, p1_4, p1_5)
        s0_1 = self.s0(p1_1)
        s0_2 = self.s0(p1_2)
        s0_3 = self.s0(p1_3)
        s0_4 = self.s0(p1_4)
        s0_5 = self.s0(p1_5)
        print(s0_1, s0_2, s0_3, s0_4, s0_5)
        p0_1 = self.p0(s0_1)
        p0_2 = self.p0(s0_2)
        p0_3 = self.p0(s0_3)
        p0_4 = self.p0(s0_4)
        p0_5 = self.p0(s0_5)
        print("output is :", p0_1, p0_2, p0_3, p0_4, p0_5)

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
    obj = Security()
    obj.run()
    # print('\n,\n'"input is: 36123")
    #
    # print("output is: 13471")
    #
    # str= input('\n\n\n'"Do you want to check the initial and final data after decryption?")
    # if str == 'yes':
    #     print("They are equal")
    # else:
    #     print("Bye")


