def func(num1, num2):
    print("print 2 parameters: ", "number1 is : ", num1, "number2 is :", num2)


# If the number of arguments is unknown, add a * before the parameter name
def func2(*num):
    print("num1 :", num[0], "\n", "num2 :", num[1], "\n", "num6 :", num[5])


def func3(num1, num2):
    print(num1, "\n", num2)


# If the number of keyword arguments is unknown, add a double ** before the parameter name
def func4(**kids):
    print("this is firs :", kids["name"], "\n", "this is phone number :) :", kids["number"])


# Default Parameter Value
def func5(name="mahdi"):
    print("name :", name)


# for in function
def func6(food):
    print("foods :")
    for i in (food):
        print("\n", i)


# function with return
def func7(number=10):
    return 10 * number


# pass for evoiding error
def func8():
    pass


# call function without pass demonstraite error
#def func9(number=10):


if __name__ == '__main__':
    func(10, 20)
    func2(1, 2, 3, 4, 5, 6, "salam", 7, 8, 9, 10)
    func3(num1=100, num2=200)
    func4(name="mahdi", number="09139935292")
    func5("mohammad mahdi")
    func5()
    foods = ["apple", "orange", "banana"]
    func6(foods)
    print(func7(20))
    func8()
    #func9()