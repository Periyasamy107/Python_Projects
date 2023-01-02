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

