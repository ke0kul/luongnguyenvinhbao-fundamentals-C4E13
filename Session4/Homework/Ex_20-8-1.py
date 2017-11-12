sentence = 'ThiS is String with Upper and lower case Letters'

sentence = sentence.lower()

import string
alphabet = string.ascii_lowercase

char_list = {}

for i in sentence:
    if i in alphabet:
        if i in char_list:
            char_list[i] += 1
        else:
            char_list[i] = 1
keys = char_list.keys()
for i in sorted(keys):
    print(i, char_list[i])
