'''1. wap to create a dict that contains following sequence
1 : 1
2 : 4
3 : 9
4 : 16
...
100 : 10000
hint: use for loop, dont do this manually
'''

'''2. WAP to sort a dictionary of 5 elements.
You can put anything inside the dictionary
'''

# sort by keys 
colors = {
    'R': 'red',
    'G': 'green',
    'B': 'blue',
    'Y': 'yellow',
    'Bk': 'black',
}

print(dict(sorted(colors.items())))