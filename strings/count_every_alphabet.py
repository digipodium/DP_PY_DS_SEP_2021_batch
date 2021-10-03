from string import ascii_lowercase

content = '''
The black skimmer (Rynchops niger) is a tern-like 
bird in the gull family Laridae, breeding in North 
and South America. Skimmers have the lower mandible 
(jawbone) and bill longer than the upper ones, which 
allows them to fly low over the water surface, skimming 
the water for small fish, insects, crustaceans and molluscs.
This black skimmer was photographed fishing while in
flight over the Rio Negro in the Pantanal, 
an area of tropical wetland in southwestern Brazil.
'''

num_of_a =content.count('a')
print(f'a occurs {num_of_a} times')

in_counter = content.count('in')
print(f'`in` occurs {in_counter} times')

# counting all alphabets

max_freq = 0
most_freq_letter = ''
for letter in ascii_lowercase:
    counter = content.casefold().count(letter)
    print(f'{letter} found {counter} times')
    if max_freq < counter:
        max_freq = counter
        most_freq_letter = letter

print(f"the {most_freq_letter} has highest frequency: {max_freq}")
