
'''   # ordered , changable , allow duplicates
list = ["sam",'lina',56,67.8,'true',90]

print(list)
print(len(list))
print(type(list))
print(list[1])
print(list[1:4])
print(list[3:])
print(list[:3])
print(list[-4:-1])
print(list[:-3])   '''

''' list = ["sam",'lina',56,67.8,'true','lina',90]

list[0] = 77

print(list)

list[1:4] = [1,'biggod','True',4,5,6]

print(list)
print(len(list))

list.insert(1,'god')

print(list)

a = [14,15,16,'you']
list.append(a)
list.append(678)
print(list)  '''

""" res = [number for number in range(1,6)]
print(res) """

""" List = [1,'sam',True,4.56]
res = [print(i) for i in List ]
print(res) """

""" res = [i for i in range(1,11)]
print(res) """

""" odd_even = [(i,'even') if i%2==0 else (i,'odd') for i in range(1,11)]
print(odd_even) """

""" name = 'ssaammmyyyyy'
res = [i for i in name if name.count(i)==2 ]
print(res) """

""" res = [i for i in range(1,11) if i==3 or i==5 or i==7 or i==1 or i==9 or i==11 ]
print(res) """

""" res = ['even' if i%2==0 else 'odd' for i in range(1,11)]
print(res) """

""" name = 'biggod'
res = [ i for i in name]
print(*res) """

""" numbers = [ i for i in range(1,11)]
print(numbers) """

""" num = [ i for i in range(1,11) if i%2==1]
print(num) """

""" even = [ i for i in range(1,11) if i%2==0]
print(even) """

""" name = 'biggod'
up = [i.upper() for i in name]
print(up) """

""" topic = 'This Is Nice'
res = [i.swapcase() for i in topic]
print(res) """

""" name = 'biggod'
l = [i for i in name]
print(l) """

""" l = [i for i in range(1,11)]
print(l) """

""" l = ['even' if i%2==0 else 'odd' for i in range(1,11)]
print(l) """

""" l = [i for i in range(1,5)]
print(l) """

""" l = [ i.upper() for i in 'biggod']
print(l) """

""" l = ['sam',45,'God','good',7.87]

# l.append(23.23)
# print(l)

# l.extend(['sam',34,3,8])
# print(l)

# l.reverse()
# print(l)

# a = l.copy()
# print(a)

l.clear()
print(l) """

