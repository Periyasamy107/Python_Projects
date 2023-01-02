""" # Print the prime number from given starting and ending range
n1 = 1
n2 = 15
for i in range(n1,n2+1):
    c=0
    for j in range(1,n2+1):
        if i%j==0:
            c+=1
    if c==2:
        print(i) """

""" number = 10
for i in range(1,number+1):
    c=0
    for j in range(1,number+1):
        if i%j==0:
            c+=1
if c==2:
    print(f'{number} is prime')
else:
    print('not') """

""" n1,n2=0,1
num=5
for i in range(num+1):
    print(n1,end=' ')
    res=n1+n2
    n1=n2
    n2=res """

