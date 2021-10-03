# str find() function allows to pass the 
# starting index, and stop index for use

data ='''What are the codes for the safe.
How safe is the safe.
Is the safe really safe?
'''

print("for loop - not good")
start_idx = 0
for i in range(5):            # use str.count() method for better output
    idx = data.find('safe',start_idx)
    print(f"`safe` word found at {idx}")
    start_idx = idx + 1


print('while loop - better')
start_idx = 0
while True:
    idx = data.find('safe',start_idx)
    if idx == -1:
        break
    print(f"`safe` word found at {idx}")
    start_idx = idx + 1    
