
num = [12,34,67,89]
num2 = [34,56,12,45]
num3 = [1,2,2,2,2,3,4,4]
for i,j in zip(num, num2):
    print(i,j)

for i,j in zip(num, num2):
    print(i + j)


for i,j,k in zip(num,num2,num3):
    print(i,j,k)