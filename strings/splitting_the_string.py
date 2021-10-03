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




