def recursive_fibonacci(n):
    if n <=1:
        return n

    else:
        return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))

def print_fibo(n):

    if n == 0:
         print("invalid entry")

    elif n == 1 or n == 2:
        print("1")

    else:
        for i in range(n):
            print(recursive_fibonacci(i))


if __name__ == '__main__':
    number = int(input("Enter your number :"))
    result = recursive_fibonacci(number)
    print_fibo(result)

