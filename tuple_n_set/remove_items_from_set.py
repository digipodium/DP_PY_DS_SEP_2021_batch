words = {'Alex','Alan','Alexa','Alexander','Xander','Thunder'}
print(words)

if 'Alan' in words:
    words.remove('Alan')
print(words)

remvd_value = words.pop()
print(words)
print(remvd_value)

words.clear()
print(words)