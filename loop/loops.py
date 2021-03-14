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

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finished")

#Nested Loops
adj=['good','nice','delicious']
fruites=['banana','apple']
for x in adj:
    for y in fruites:
        print(x)
        print(y)
print("Changing.......")
adj=['good','nice','delicious']
fruites=['banana','apple']
for x in adj:
    for y in fruites:
        print(x)
    print(y)

print("Changing2.......")
adj=['good','nice','delicious']
fruites=['banana','apple']
for x in adj:
    print(x)
    for y in fruites:
        print(y)

print("Changing3.......")
adj=['good','nice','delicious']
fruites=['banana','apple']
for x in adj:
    for y in fruites:
        print(x,y)

#loop with pass
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [1,2,3]:
    pass
print("End for.................")
#while
count=0
while count<10:
    print(count)
    count+=1
else:
    print("Finished while")

print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d :
    print("%s  %d" %(i,d[i]))