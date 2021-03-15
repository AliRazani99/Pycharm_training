class Test:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def print(self):
        print("name is : ", self.name, '\n', "last name is :", self.last_name)


if __name__ == '__main__':
    name = input("Enter your name :")
    last_name = input("Enter your last name :")
    obj = Test(name, last_name)
    obj.print()
