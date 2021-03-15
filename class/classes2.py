class Test:

    answer=0
    first=0
    second=0

    def __init__(self):
        self.name = "mahdi"
        self.last_name = "omid"


    def calculator(self):
        self.answer=self.first + self.second

    def print(self):
        print(" Name is :",self.name ,'\n',"Last name is :",self.last_name)
        print(" Sumation of",self.first,"and",self.second,"is :",self.answer)



if __name__ == '__main__':
    test=Test()
    test.first=100
    test.second=200
    test.calculator()
    test.print()
