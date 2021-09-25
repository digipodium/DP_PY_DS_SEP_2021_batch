"""
for temp_var in iterable:
    statement 1
    statement 2
    ...
    statement n

iterables can be of
- string
- list
- tuple
- set
- dict
- special functions like range(),zip(),enumerate()
- anything with multiple elements
"""

num = [1,2,3,4,5,6,7,19,12]
for i in num:
    print(i)

msg = "We are now using loops"
print('characters in msg:',len(msg))

# traversal 
for char in msg:
    if char != ' ':
        print(char)

# numeric loop
for i in range(10):
    print(i, end=',')