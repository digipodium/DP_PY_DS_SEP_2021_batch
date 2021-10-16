x = {1,2,3,5,4,6,7,8,9,0}
y = {2,4,1,5}
z = {11,12,13,14}
a = {1,2,3,99,60}

print('x is superset of y', x.issuperset(y))
print('x is superset of z', x.issuperset(z))
print('x is superset of a', x.issuperset(a))

print('y is subset of x', y.issubset(x))
print('z is subset of x', y.issubset(z))
print('a is subset of x', y.issubset(a))

print('a is unrelated to x', a.isdisjoint(x))
print('a is unrelated to y', a.isdisjoint(y))
print('a is unrelated to z', a.isdisjoint(z))

