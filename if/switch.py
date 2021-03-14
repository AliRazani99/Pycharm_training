#Switchers
def func(argument):
    switchers ={

        0 : "Zero",
        1 : "One",
        2 : "Two",
        3 : "Three"

    }
    print(switchers.get(argument,'nothing'))

if __name__ == '__main__':
    func(2)
    func(5)