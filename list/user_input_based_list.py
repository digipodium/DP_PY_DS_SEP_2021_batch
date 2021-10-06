# wap to take user input to create a list
# the user should decide the size of list
# the list should be numeric
# display list values and sum , min, max, mean of the list

numbers = []

limit = int(input('enter size of list>>'))
for i in range(limit):
    val =  int(input(f'{i+1}>>>'))
    numbers.append(val)

print("You entered the following values")
print(numbers)
print("sum >>",sum(numbers))
print("max value >>",max(numbers))
print("min value >>",min(numbers))
print("mean value >>",sum(numbers)/len(numbers))
