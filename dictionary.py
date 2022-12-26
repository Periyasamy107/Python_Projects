
""" # unordered, unchangable , not allow duplicates

dictt = {
    'name' : 'sam' ,
    'age'  : 38 ,
    'gender' : 'male' ,
    'interest' : ['playing','sleeping',1000]
} 

# Keys don't allow the duplicate but values can allow the duplicates

print(dictt)
#printing the value in two methods
print(dictt['gender'])
print(dictt.get('gender'))
#above two methods are print in python
print(dictt['interest'])
print(len(dictt))
# two methods of updating the values
# 1) normal method
dictt['age'] = 10
print(dictt)
# we can update only one value at a time
# 2) update method
dictt.update({'gender':'male111','interest':'nothing'})
print(dictt)
# by update method we can update more than one value at a time

dictt['color'] = 'red' 
print(dictt)

dictt.pop('gender')
print(dictt)  """

""" dictionary = {1:'apple',2:'orange',3:'banana'}

print(dictionary[1])

print(dictionary[2])

print(dictionary[3])

print(dictionary.keys())

print(dictionary.values())

print(dictionary.items()) """

""" d = { 'name' : 'samy', 'age' : 46}
print(d.items())
print(d.values())
print(d.keys())   """

""" d = {'name':'sam','age':45}
# print(d)

# a = d.copy()
# print(a)

# print(d.get('ages','not found'))

# d.popitem()
# print(d)

# d.pop('name')
# print(d)

# d.update({'salary' : 4500})
# print(d)

# e = ('name1','name2')
# f = ('sam')
# g = dict.fromkeys(e,f)
# print(g)

# e = d.setdefault('name','lina')
# print(e) 

d.clear()
print(d)

del d 
print(d) """

d = {'name':'biggod','age':45}

# e = d.copy()
# print(e)

# print(d.get('age','not found'))

# d.popitem()
# print(d)

# d.pop('name')
# print(d)

# print(d)

# d.update({'salary':8900})
# print(d)

