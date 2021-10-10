'''
- comprehension -> when we want to create a list from an existing list in 1 line
- mapping -> generate same size sequence from existing sequence
- filtering -> create a smaller sequence from existing one, using a condition
'''

# mapping without comprehension
x = [1,2,3,4,5,6,7,8,9,10]

x2 = []
for i in x:
    sqr = i ** 2
    x2.append(sqr)

print(x)
print(x2)

# filter without comprehension

x_even = []
for i in x:
    if i%2 == 0 :
        x_even.append(i)

print(x)
print(x_even)
