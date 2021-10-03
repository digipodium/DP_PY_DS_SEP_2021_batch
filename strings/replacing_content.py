msg = '''Skimmers have the lower jaw 
and bill longer than the upper ones, which 
allows them to fly low over the water surface, skimming 
the water for small fish, insects, crustaceans and molluscs.
'''
print(msg)

updated_msg = msg.replace('the','wah')
print(updated_msg)

updated_msg = msg.replace('a','u')
print('replaced a\n',updated_msg)

# remove via replace
updated_msg = msg.replace('c','')
print('replaced c\n',updated_msg)

