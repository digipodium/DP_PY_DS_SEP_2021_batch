class Movie:

    def __init__(self,name, genre, year):
        self.name = name # instance variable
        self.genre = genre
        self.year = year

    def show(self):
        print('Details:',self.name,"/".join(self.genre),self.year)


m = Movie('Free Guy',['Comedy','Action'],2021)
m2 = Movie("Dune",['Scifi','Drama'],2021)

m.show()
m2.show()
