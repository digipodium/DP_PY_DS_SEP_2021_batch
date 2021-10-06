num = list(range(20))

print(num)

print('first value',num[0]) 
print('second value',num[1]) 
print('last value',num[-1]) 

num[0] = 50 # updated the 0 idx value to 50
num[-1] = 20 # updated the last idx value to 20
num[2] = 20 # updated the 2 idx value to 20
# updated
print(num)

print('first 3 items',num[:3])
print('last 5 items',num[-5:])
print('all items except first 2 and last 2',num[2 : -2])
print('reverse a list',num[::-1])
print('all even indexes of list',num[::2])
print('all odd indexes of list',num[1::2])