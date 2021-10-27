#  we have to make a class for storing information about cake

class Cake:
    brand = "JJ Bakery"
    flavour ='Chocolate'
    weight = 1
    is_eggless = False
    color = 'brown'


cake1 = Cake() # object 1
sasta_cake = Cake() # object 2

sasta_cake.flavour = "Strawberry"
sasta_cake.brand = "chandu bakery"
sasta_cake.color = 'pink'
sasta_cake.is_eggless = True
sasta_cake.weight = .25

print(cake1.flavour)
print(sasta_cake.flavour)

# redundant coding
# lenght lines
# solution -> intro to constructor