'''
# find -> better
# index
'''
msg = 'Once upon a time, their was a kingdom. the king was Richard'

idx = msg.find('time')
print(f'`time` was found at index {idx}')
idx = msg.find('queen')
print(f'`queen` was found at index {idx}')
if idx == -1:
    print(f'`queen` was not found')

idxKing = msg.find('king')
print(f'`king` was found at index {idxKing}')

idxA = msg.find('a')
print(f'`a` was found at index {idxA}')
print(len(msg))