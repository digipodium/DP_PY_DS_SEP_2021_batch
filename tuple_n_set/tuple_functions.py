mytuple = 12,123,123,13,1,13,1,31,2312,3,13,132,1,31,31,2

print(mytuple.count(1),'occurances of 1')
print(mytuple.index(2312),'index has 2312')

for i in mytuple:
    print(i, end=' ')
print('\nreversed')
for i in mytuple[::-1]:
    print(i, end=' ')