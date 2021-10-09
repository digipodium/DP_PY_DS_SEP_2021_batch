x = [1,2,3,3,1,2,3,2,1,3,1,2,3,3,1,2,3,2,3,1,2,1,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3,1,2,3]
print(x)

print("occurance of 1=",x.count(1))
print("occurance of 2=",x.count(2))
print("occurance of 3=",x.count(3))
print("occurance of 5=",x.count(5))
print("occurance of 10=",x.count(10))

a = ['chicago','new york','dallas']
b = [12,45,13]
c = ['Nevada',57,'Massouri',58]
print(a)
a.sort()
print(a)

print(b)
b.sort(reverse=True)
print(b)
# error
# print(c)
# c.sort()
# print(c)

y = [1,1,12,1,1123,1223,1232,2,2,2,3,3,3,3,]
print(y)
y.reverse()
print(y)
y.reverse()
print(y)
idx = y.index(1223)
print('1223 found at',idx)
idx = y.index(2)
print('2 found at',idx)

if 123 in y:
    idx = y.index(123)
    print('123 found at',idx)

z = x.copy()
print(z)
print(x)
x.sort()
print(x)
print(z)

