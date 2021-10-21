import string
import json

f = open('pokemon_full.json')
s = f.read()
plist = json.loads(s)

print('1: ', len(s))
print('2: ', len(s.translate(s.maketrans(dict.fromkeys(string.punctuation))).replace(' ', '')))

s = ''
name = ''
for obj in plist:
    if len(obj['description']) > len(s):
        s = obj['description']
        name = obj['name']
print('3: ', name)

words_num = 0
abilities = []
for obj in plist:
    for abil in obj['abilities']:
        if len(abil.split()) > words_num:
            words_num = len(abil.split())
            abilities = []
        if len(abil.split()) == words_num:
            abilities.append(abil)
print('4: ', abilities)
f.close()
