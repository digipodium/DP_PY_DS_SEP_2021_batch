marks = {
    'rohan':2,
    'rehan':2,
    'sohan':3,
    'mohan':5,
    'ali':10,
    'alex':0,
}

names=list(marks.keys())
print(names)

numbers=list(marks.values())
print(numbers)

items=list(marks.items())
print(items)

a = "Ramu"
b = "Shamu"
c = "Lalita"
d = "Jaya"
e = "Sushma"

default_marks = 'N/A'

new_students = dict.fromkeys([a,b,c,d,e], default_marks)
print(new_students)

positions = list(range(1,11))
position_dict = dict.fromkeys(positions,"available")
print(position_dict)

copy_of_dict = position_dict.copy()
print(copy_of_dict)