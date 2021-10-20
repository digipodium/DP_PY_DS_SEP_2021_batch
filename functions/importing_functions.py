import file_function as ff

data = ff.reader('radiants.txt')
print(len(data),' chars in file')

data = ff.reader('dummy.txt')
print(len(data),' chars in file')