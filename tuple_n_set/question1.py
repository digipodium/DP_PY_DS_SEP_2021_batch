# wap to add values from user in a set.
# the can add any number of values in the set
# use while loop to perform this task
# time 10 min.

data = set()

while True:
    x = input('enter a value:')
    if not x:
        break
    data.add(x)

print(data)