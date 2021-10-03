msg = "we will be seeing the horizon"

words = msg.split()
print(words)

msg2 = 'Hi there, how are you? where have you been?'
sentences = msg2.split(',')
print(sentences)

sentences = msg2.split('?')
print(sentences)

gibberish = msg2.split('a')
print(gibberish)

print(f"we found {len(words)} words in msg")
print(f"we found {len(msg2.split())} words in msg2")

msg3 = 'welcome to wakanda, you will have fun, just dont steal from us, or you will have no fun'

print('n ->', msg3.split(','))
print('n 2 split ->', msg3.split(',', maxsplit=2))
print('r ->', msg3.rsplit(','))
print('r 2 split ->', msg3.rsplit(',', maxsplit=2))

print(msg3[:18])




