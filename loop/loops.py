# loop in string
string = 'banana'
for x in string:
    print(x)

# loop in list
fruites = ['apple', 'banana', 'orange']
for x in fruites:
    print(x)

# loop with continue
fruites = ['apple', 'banana', 'orange']
for x in fruites:
    if x == 'banana':
        continue
    print(x)

# loop in range
# Note that range(20) is not the values of 0 to 6, but the values 0 to 19.
for x in range(20):
    print(x)

# range(2, 6), which means values from 2 to 6 (but not including 6):
for x in range(2, 6):
    print(x)

# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)

#Else in For Loop
#Note:The else block will NOT be executed if the loop is stopped by a break statement
for x in range(5):
    print(x)
else:
    print("Finished")

