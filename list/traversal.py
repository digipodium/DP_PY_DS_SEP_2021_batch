num = list(range(5,15))

for element in num:
    print(element)

words = ['This','That','Wish','What','Word']
for item in words:
    print(f'{item} is {len(item)} chars')


coords = [[1,2],[2,3],[3,5]]
for i in coords:
    print(i)

for i in coords:
    print(i[0], i[1])

for idx, value in enumerate(words):
    print(f'{idx} has {value}')

for i in num:
    if i % 3 == 0:
        print(i)

for items in coords:
    for i in items:
        print(i)