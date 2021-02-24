#just for practice
my_list=["mahdi" , "sara" , "lia" , "reza" ]
print("my list is: " , my_list)
print(len(my_list))
print(my_list[0])
print(len(my_list[2]))

second_list=["mahdi",True,2,False,"male"]
print(second_list)
print(second_list[2],second_list[3],second_list[2])
print(type(my_list))

third_list=list(("mahdi", True , False , 2 , "sara","omid",False,True,2,"askari"))
print(third_list)

last_list=["mahdi",[1,2,3,4,"mahdi"],True,['a']]
print(last_list[1][2])

#fruits:)
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("fruits :",fruits)
print("apple count :",fruits.count('apple'))

print("tangerine count :",fruits.count('tangerine'))

print("banana index :",fruits.index('banana'))

print("banana next index :",fruits.index('banana', 4))  # Find next banana starting a position 4

print("reverse :",fruits.reverse())

print("append grape :",fruits.append('grape'))

print("sort fruits:",fruits.sort())
print(fruits)

print("pop :",fruits.pop())
print(fruits)