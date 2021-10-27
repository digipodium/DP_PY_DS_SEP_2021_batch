
class IceCream:

    def __init__(self,flavor,price,brand,style):
        self.flavor = flavor
        self.price = price
        self.brand = brand
        self.style = style
        print("ice cream created")


#  object
ic1 = IceCream('chocolate',30,'Amul','bar')
ic2 = IceCream('vanilla',25,'Quality walls','cone')

print(ic1.brand, ic1.flavor)
print(ic2.brand, ic2.flavor)