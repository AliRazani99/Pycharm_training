fp = open('test_file.txt', 'w')
fp.write("salam")
fp.close()
fp= open('test_file.txt', 'r')
dic = {}
lines = fp.readlines()

for line in fp:

  words = line.split()

  for x in words:

    dic.append(x)

for i in range(0,len(dic)):

  count = 1

  for j in range(i+1 , len(dic)):

    if dic[i] == dic[j]:

       count+=1

  print((dic[i],count))
  print('%s,%s'%(dic[i]),count)