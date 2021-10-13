a = {1,2,3}

a.add(129)
a.add("Charbagh")
a.add((1,2,3))
print(a)
# error -> u cannot add a list, dict or set in a set
# a.add([1,2,3])
# print(a)

x = [1,2,3,3,3,1,231,3,12]
a.update(x)
print(a)

