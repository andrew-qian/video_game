"""
# example 1

# no loop
x = 0
x = 1
x = 2
x = 3
x = 4

# with loop
for x in range(5):
    None

# example 2

# no loop
a = 2

x = 0
a = 3

x = 1
a = 4

x = 2
a = 5

x = 3
a = 6

x = 4
a = 7

# with loop
a = 2
print('a', a)
print()
for x in range(5):
    a = a + 1
    print('x', x)
    print('a', a)
    print()


# example 3

# no loop
a = 1

x = 0
a = 3

x = 1
a = 5

x = 2
a = 7

x = 3
a = 9

x = 4
a = 11

# with loop
a = 1
print('a', a)
print()

for x in range(5):
    a = a + 2
    print('x', x)
    print('a', a)
    print()


# example 4
a = 3

x = 0
a = 3  # first add 0

x = 1
a = 4  # then add 1

x = 2
a = 6  # then add 2 

# with loop
a = 3
print('a', a)
print()

for x in range(3):
    a = a + x
    print('x', x)
    print('a', a)
    print()

# example 4
# print out the following using a loop
0
2
4
6
8

for x in range(5):
    a = x * 2
    print(a)

# example 5
# these are the same loop
for x in range(5):
    print(x)
    
for x in [0, 1, 2, 3, 4]:
    print(x)   
    
"""
 
# example 6    
# what are the final values of a and b
a = 1
b = 2

for x in range(3):
    a = a + b

print('my guesses')
print('a', 7)
print('b', 2)

print()

print('actual values')
print('a', a)
print('b', b)
    
    
    
    
    
    
    
    
    
    
    
    

	



















