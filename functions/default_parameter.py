def summer2(a,b,c,d=0):
    return a + b + c + d

print( summer2(1,2,3,4) )
print( summer2(2,3,1) )
print( summer2(a=1,b=2,c=3) )
print( summer2(a=1,b=2,c=3, d=4) )
print( summer2(1,2,3,d=4) )

# always put default parameter after
# required parameter

def triangle(b=1,h=1):
    return 1/2 * b * h

print(triangle())
print(triangle(b = 10))
print(triangle(b = 10, h = 5))
print(triangle(h = 5))
print(triangle(h = 5, b = 5))
print(triangle(2,3))
print(triangle(2))
print(triangle(3))
print(triangle(3,2))
