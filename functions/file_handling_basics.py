'''
file handling basics
1. read a file - open()
2. write a file - open()
3. update a file - open()
open() function has a option to set mode of file
it returns a file object
'''

file = open('dummy.txt')
print(file.read())
file.close()

f1 = open('radiants.txt','w')
f1.write("The radiants are saviors of humanity\n")
f1.write("they have shardplate and shardblade\n")
f1.write("To be continued\n")
f1.close() # save

f2 = open('dummy.txt','a')
f2.write("\n Written by Knowledgeable person")
f2.close()