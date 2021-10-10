x = [12,34,56,67,89,90]
words = "Python is the best language for coding".split()

'''
map() - modern way for mapping a sequence for a operation in 1 line
filter() - modern way for filtering a sequence using condition in 1 line
'''

'''
map() and reduce() use lazy objects concept, in which data is not
consuming memory until it is casted to a particular datatype like
list, tuple, set
'''

x2 = list(map(lambda i : i ** 2, x))
y = [2,5,7,8,3,10]

xy = list(map(lambda i,j: i + j, x, y))
print(xy)

f = lambda i,j: i + j
if len(x) == len(y):
    xy = list(map(f, x, y))
    print(xy)


# filter

words_with_a = list(filter(lambda i: "n" in i, words ))
print(words_with_a)

