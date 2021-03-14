# Switchers
def func(argument):
    switchers = {

        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three"

    }
    print(switchers.get(argument, 'nothing'))


def func2():
    while (True):
        string = input("Enter your string :")
        switchers = {
            'A': 1,
            'B': 2,
            'C': 3,
            'D': 4
        }
        print(switchers.get(string, 'nothing'))
        if string == 'q':
            break


if __name__ == '__main__':
    func(2)
    func(5)
    func2()
