x = {1,2,3,11,23}
y = {1,2,3,5,6}

common = x.intersection(y)
print("x and y have",common)

xuniq = x.difference(y)
yuniq = y.difference(x)
print("x has unique values",xuniq)
print("y has unique values",yuniq)

# not to be used in code actually
x.intersection_update(y)
print(x)

y.difference_update(x)
print(y)