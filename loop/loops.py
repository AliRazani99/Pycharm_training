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
#Note that range(20) is not the values of 0 to 6, but the values 0 to 19.
for x in range(20):
    print(x)

