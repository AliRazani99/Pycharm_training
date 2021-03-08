x= eval(input('enter the begininig' ))

y = eval(input('enter the end of your numbers'))

for i in range(x,y+1):

  count = 0

  for j in range(2,i):

      if i%j == 0:

          count+=1

  if count == 0:

     print(i)




