class ListStat(list): # subclass of list
    
    def sum(self):
        return sum(self)

    def mean(self):
        return self.sum()/len(self)


x = ListStat((1,2,3,4))
x.append(10)
x.append(20)
print(x.sum())
print(x.mean())