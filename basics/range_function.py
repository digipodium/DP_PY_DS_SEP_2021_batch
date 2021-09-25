'''
range(end)
range(start,end)
range(start,end, gap)
'''
print('normal')
for i in range(5):
    print(i, end=" ")

print('\n style 2')
for i in range(5,15):
    print(i, end=' ')

print('\n style 3 with gap')
for i in range(3,15,2):
    print(i,end=' ')
