# python has different operator 
# 1. Mathematical
# 2. Condition
# 3. Assignment 
# 4. logical
# 5. membership
# 6. instance ❌
# 7. walrus ❌

# mathematical operators 
a = 10 * 3
print(a)
a = 10 / 3  # division - real number
print(a)
a = 10 // 3  # integer division - quotient
print(a)
a = 10 % 3   # modulus-  remainder
print(a)
a = 10 ** 3  # exponent
print(a)
a = 10 + 3
print(a)
a = 10 - 3
print(a)

# comparison operator
a = 10
b = 3
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
print(a == b)
print(a != b)

# assignment operator
c = 15
print(c)
c += 10  # add 10 to existing value of c
print(c)
c -=10   # subtract 10 from existing value of c
print(c)
c *= 10
print(c)
c /= 10
print(c)
c //= 10
print(c)
c %= 10
print(c)
c **= 10
print(c)

# logical operator - multiple expression [and , or , not]
a = 5
b = 15
c = 10
print( a > b and a > c)
print( b > a or b > 100)
print(not a > b)
print(a > b and a < c or a > 10)

# membership operator - in [it can search a value in a iterable]

colors = ['red','blue','green','purple','yellow']

print('red' in colors)
print('brown' in colors)
print('orange' in colors)
print(45 in colors)

     