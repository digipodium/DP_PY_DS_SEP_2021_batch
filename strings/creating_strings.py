
name = 'Alex mason'
city = "New york"

story = '''this is a story about
alex mason, okay!
this guy is so good
that i cant tell you.'''

poem = """
johnny johnny, yes papa
eating sugar, yes papa
thats okay, you did not lie
"""

print(type(name), type(city), type(story), type(poem))

print(name)
print(city)
print(story)
print()         # line change
print(poem)

properties = '''
1. indexed
2. immutable
3. str() is the contructor for creating strings [type cast]
4. it can be concatenated using +
5. it can be duplicated using *
'''

print(properties)

name[0] = 'B' # will not work as strins are immutable