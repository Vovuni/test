import string
import json

f = open('pokemon_full.json')
str = f.read()
f = open('pokemon_full.json')
jsn = json.load(f)

print('1: ', len(str))

print('2: ', len(str.translate(str.maketrans(dict.fromkeys(string.punctuation))).replace(' ', '')))

str = ''
name = ''
for obj in jsn:
    if len(obj['description']) > len(str):
        str = obj['description']
        name = obj['name']
print('3: ', name)

words_num = 0
abilities = []
for obj in jsn:
    for abil in obj['abilities']:
        if len(abil.split()) > words_num:
            words_num = len(abil.split())
            abilities = []
        if len(abil.split()) == words_num:
            abilities.append(abil)
print('4: ', abilities)
