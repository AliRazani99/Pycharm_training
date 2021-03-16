class Search:
    # just for get 5 number from input
    def get_data(self):
        x = 0
        my_array = []
        count=int(input("How many numbers do you wanna add?"))
        while (x < count):
            number = int(input("please inter your number:"))
            my_array.append(number)
            x += 1

        print("my array is :", my_array)
        return my_array

    # for sorting data
    def selection_sort(self, my_array):

        for x in range(len(my_array)):
            for y in range(x + 1, len(my_array)):
                # finding minimum and swapping
                if my_array[x] > my_array[y]:
                    temp = my_array[x]
                    my_array[x] = my_array[y]
                    my_array[y] = temp

        return my_array

    # just for print data
    def print_sorted(self, my_array):
        print("my sorted array is :", my_array)


if __name__ == '__main__':
    obj = Search()
    my_array = obj.get_data()
    obj.print_sorted(obj.selection_sort(my_array))
