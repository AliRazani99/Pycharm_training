class Sort:
    # just for get 5 number from input
    def __init__(self, array):
        self.array = array

    # for sorting data
    def selection_sort(self):

        for x in range(len(self.array)):
            for y in range(x + 1, len(self.array)):
                # finding minimum and swapping
                if self.array[x] > self.array[y]:
                    temp = self.array[x]
                    self.array[x] = self.array[y]
                    self.array[y] = temp
        print("my sorted array is :", self.array)


if __name__ == '__main__':
    # get data
    x = 0
    my_array = []
    count = int(input("How many numbers do you wanna add?"))
    while (x < count):
        number = int(input("please inter your number:"))
        my_array.append(number)
        x += 1
    print("my array is :", my_array)

    obj = Sort(my_array)
    obj.selection_sort()
