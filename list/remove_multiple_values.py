x = [
    1,2,3,3,1,2,3,2,
    1,3,1,2,3,3,1,2,
    3,2,3,1,2,1,3,1,
    2,3,1,2,3,1,2,3,
    1,2,3,1,2,3,1,2,
    3,1,2,3,2,5,7,3
    ]
print(x)
y =  x.copy()
# remove all the 3s in this list
for i in range(x.count(3)):
    x.remove(3)

print("Removed All 3s")
print(x)

# removing all 3s with pop n index
while 3 in y:
    idx = y.index(3)
    y.pop(idx)
print(y)