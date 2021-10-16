words = {} # dict

words['alpha'] = "number one, the starting value, or the top value" 
print("User input-->")
for i in range(3):
    k = input('enter a word->>')
    v = input('enter the meaning->>')
    words[k] = v

# full 
print(words)

# reading a particular value
print(words['alpha'])
print(words.get('alpha','not found'))
print(words.get('beta'))
print(words.get('beta','🙈'))



