'''
trivia
2 types of function
- function that will give output
- function that will change the original variable
'''
name =  "we are going to have FUN"
print(name)

uname = name.upper()
print('upper->',uname)

lname = name.lower()
print('lower->',lname)

n1 = name.capitalize()
print('captalize->',n1)

n2 = name.title()
print('title->',n2)

n3 = name.swapcase()
print('swapcase->',n3)

n4 = name.casefold() # same as lowercase
print('casefold->',n4)

word = input('what animal do you like :')
spacing =  int(input('select a number for spacing: '))
print(f'printing {word} with spacing {spacing}')

lword = word.ljust(spacing)
print(lword)
rword = word.rjust(spacing)
print(rword)
cword = word.center(spacing)
print(cword)

char =  input('enter a character')
lword = word.ljust(spacing,char)
print(lword)
rword = word.rjust(spacing,char)
print(rword)
cword = word.center(spacing,char)
print(cword)