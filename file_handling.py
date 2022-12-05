
'''f = open('sample1.txt','r')

#print(f.read())
#print(f.read(15))
print(f.readline())
print(f.readline())
print(f.readline(1))  

for a in f:
    print(a)

f.close()   '''

'''   f = open('sample1.txt','a')
f.write('this is wonderful')
f.close()

f = open('sample1.txt','r')
print(f.read())   '''

'''   f = open('sample1.txt','w')
f.write('This is wonderful \t ')
f.write('samy \n')
f.write('Nice to see you \n')
f.write('Is it so.')
f.close()

f = open('sample1.txt','r')
print(f.read())   '''

'''   f = open('sample3.txt','x')
f.write('good to see you agin and agin in here this situation')
f.close()

f = open('sample3.txt','r')
print(f.read())   '''

'''   f = open('open_new.txt','w')
f.write('new file created by write function')
f = open('open_new.txt','r')
print(f.read())   '''

""" import os

if os.path.exists('open_new.txt'):
    os.remove('open_new.txt')

if os.path.exists('sample1.txt'):
    os.remove('sample1.txt')

if os.path.exists('sample2.txt'):
    os.remove('sample2.txt')

if os.path.exists('sample3.txt'):
    os.remove('sample3.txt') """

""" newfile = open('sample.txt','w')
newfile.write('This is my sample file')
newfile.write('\nPeriyasamy is a good boy he is smart')
newfile.write('\nhe is smart')
newfile.close() """

""" filename = 'sample.txt'
file = open(filename,'r')
data = file.readlines()
print(data)
file.close() """

""" filename = 'sample.txt'
with open(filename,'r') as file:
    #data = file.read()
    #data = file.readline()
    data = file.readlines()
    print(data) """

""" filename = 'newfile.txt'
with open(filename,'w') as file:
    file.write('good\n')
    file.write('nice') """

""" fruits = ['apple','orange','banana']
filename = 'newfile.txt'
with open(filename,'w') as file:
    file.writelines(fruits) """

""" fruits = ['apple','orange','banana']
filename = 'newfile.txt'
with open(filename,'w') as file:
    for fruit in fruits:
        file.write(fruit + '\n') """

""" fruits = ['banana','orange']
filename = 'newfile.txt'
with open(filename,'a') as f:
    for fruit in fruits:
        f.write(fruit + '\n') """

""" filename = 'newfile.txt'
with open(filename,'a') as f:
    f.write('kiwi' + '\n')
    f.write('orange'+ '\n')
    f.write('strawberry' + '\n')
    f.write('orange' + '\n') """

""" with open('newfile.txt','r') as file:
    print(file.read()) """

""" filename = 'numbers.txt'
with open(filename,'w') as file:
    for number in range(101,111):
        file.write(f'{number}\n') """

""" filename = 'numbers.txt'
with open(filename,'r') as file:
    result = file.readlines()
    result = [int(number.strip('\n')) for number in result ]
    print(result)
    print(type(result)) 
    print(sum(result)) """

""" filename = 'sample.txt'
with open(filename,'w') as file:
    file.write('I am a good boy') """

""" with open('sample.txt','r') as file:
    print(file.read()) """

""" filename = 'sample.txt'
with open(filename,'r') as file:
    print(file.read()) """

""" with open('sample.txt','a') as file:
    file.write('\nI think this comment is right') """
    
"""filename = 'test.txt'
with open(filename,'w') as file:
    file.write('testttt text file') """

""" with open(filename,'w') as file:
    file.write('good')
    file.write('\nnice') """

""" with open(filename,'a') as file:
    file.write('apple\n')
    file.write('orange\n')
    file.write('pineapple\n')
    file.write('banana') """

""" filename = 'sample.txt'
file = open(filename,'r') 
#output = file.read()   #--> read all lines
#output = file.readline()  #--> read first line
output = file.readlines()  #--> read all lines and give result like list
print(output)
file.close() """

""" with open('sample.txt','r') as file:
    res = file.readlines()
    print(res) """

""" with open('sample.txt','w') as file:
    file.write('Biggod')
    file.write('\nSamy') """

""" with open('sample.txt','w') as file:
    out1 = file.write('Biggod')
    out2 = file.write('\nSamy')
    print(out1,out2) """

""" with open('sample.txt','a') as file:
    print(file.write('\norange')) """

""" fruits = ['apple','orange','banana']
filename = 'sample.txt'
with open(filename,'w') as file:
    file.writelines(fruits) """

""" fruits = ['apple','orange','banana']
filename = 'sample.txt'
with open(filename,'w') as file:
    for i in fruits:
        file.write(i+'\n') """

""" with open('sample.txt','a') as file:
    file.write('pineapple\n') """

""" with open('sample.txt','w') as file:
    for i in range(1,11):
        file.write(f'{i}\n')  """

""" with open('sample.txt','r') as file:
    print(file.readlines()) """

""" with open('sample.txt','r') as file:
    result = file.readlines()
    output = [i.strip('\n') for i in result]
    print(output) """

""" with open('sample.txt','r') as file:
    result = file.readlines()
    output = [int(i.strip('\n')) for i in result]
    print(output) """

""" with open('sample.txt','r') as file:
    result = file.readlines()
    output = [int(i.strip('\n')) for i in result]
    print(sum(output)) """

""" filename = 'sample.txt'
file = open(filename,'r')
#res = file.read()
#res = file.readline()
res = file.readlines()
print(res) """

""" with open('sample.txt','r') as file:
    out = file.read()
    print(out) """

""" with open('sample.txt','w') as file:
    file.write('Biggod') """

""" fruits = ['apple','orange']
filename = 'sample.txt'
with open(filename,'w') as file:
    file.writelines(fruits) """

""" fruits = ['orange','apple']
filename = 'sample.txt'
with open(filename,'w') as file:
    for i in fruits:
        file.write(i+'\n') """

