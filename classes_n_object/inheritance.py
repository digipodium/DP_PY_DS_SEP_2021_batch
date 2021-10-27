# parent class or super class
class Item:

    def __init__(self,color,material):
        self.color = color
        self.material = material
    

# child class or sub class
class PhysicalItem(Item):

    def __init__(self,c,m,weight,height,width):
        super().__init__(c,m)
        self.weight = weight
        self.height = height
        self.width =width

    def area(self):
        return self.height * self.width

# subclass of physical item
class SpPhysicalItem(PhysicalItem):

    def __init__(self, c, m, w, h, wd,brand,tech):
        super().__init__(c, m, w, h, wd)
        self.brand = brand
        self.tech = tech

i = Item('red','steel')
j = PhysicalItem('yellow','wood',2,2,3)
k = SpPhysicalItem('yellow','wood',3,2,3,'Plywood','Anti termite')

print(j.area(), k.area())