'''
- comprehension -> when we want to create a list from an existing list in 1 line
- mapping -> generate same size sequence from existing sequence
- filtering -> create a smaller sequence from existing one, using a condition
'''

'''syntax
newlist = [ operation loop-for-existinglist !condition!  ]
'''

x = [2,3,1,2,4,567,89,109,189]
# mapping
x2 = [i**2 for i in x]
print(x)
print(x2)

# filter
x_odd = [i for i in x if i%2 != 0]
print(x_odd)

x_odd_sqrs = [i**2 for i in x if i%2 != 0]
print(x_odd_sqrs)