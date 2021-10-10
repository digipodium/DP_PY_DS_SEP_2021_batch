'''
f(x) = x + 10 * 20
f(5) 
f(3)
'''

'''
lambda expression - are a way to write anonymous function in 1 line
'''

f = lambda x: x + 10 - x * 10
print(f(2))
print(f(3))
print(f(5))
print(f(10))

g = lambda x,y: x + y * x - y
print(g(1,2))
print(g(12,13))
print(g(123,321))