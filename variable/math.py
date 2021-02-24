
import math

def math_func( first_num,second_num):
    pow=math.pow(first_num,second_num)
    print('pow is :',pow)

    cos=math.cos(first_num)
    print('cos is: ',cos)

    sin=math.sin(second_num)
    print('sin is: ',sin)

    tan=math.tan(first_num)
    print('tan is: ', tan)

    sum=float(cos)+float(sin)+float(tan)
    print("the sum of {0} and {1} and {2} is {3}".format(sin,cos,tan,sum))

if __name__ == '__main__':
    first_num=int(input("inter your first number :"))
    second_num= int(input("inter your second number :"))
    math_func(first_num,second_num)