wiki_content = '''The marsh frog (Pelophylax ridibundus) 
is a species of amphibian native to Europe and parts of Asia. 
It is the largest type of frog in most of its range, 
growing to a snout-to-vent length of around 100 mm (4 in); 
tadpoles can reach up to 190 mm (7.5 in) in length, 
but this usually occurs in places with long winters 
where the tadpole has time to grow. Marsh frogs hibernate 
during the winter, either underwater or in burrows, 
and are able to use the Earth's magnetic field to locate 
breeding ponds. This marsh frog was photographed in Kampinos National Park, Poland.
'''
words = wiki_content.split()

max_freq = 0
mx_occ_word =''
for item in words:
    count = words.count(item)
    print(f'{item} -> {count}')
    if count > max_freq:
        max_freq = count
        mx_occ_word = item

print(f'{mx_occ_word} =>>> {max_freq}')
