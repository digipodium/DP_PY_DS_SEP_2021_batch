'''
for-else is a special variation of for loop
where we can check if the for loop completed
all iteration or not. else block will only execute
when all iteration are completed.
'''

# prime number
num = int(input('enter the number '))

for i in range(2,num):
    if num % i == 0:
        print('non prime value', num)
        break
else:
    print('Prime value',num)