# wap to find the sum of all values in a numerical list

x = [1,23,123,123,123,13,13,2]
total = 0
for i in x:
    total += i
print(x,'>> total =', total)

# short version
total = sum(x)
print(total)

# short version
x_max = max(x)
print(x_max)

# short version
x_min = min(x)
print(x_min)

# average
x_mean = sum(x) / len(x)
print(x_mean)
