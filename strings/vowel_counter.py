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

vowels = "aeiou"

for vowel in vowels:
    c = content.casefold().count(vowel)
    print(f' {vowel} -> {c} times')