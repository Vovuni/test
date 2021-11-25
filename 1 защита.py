import json
import numpy as np

f = open('pokemon_full.json')
s = f.read()
data = json.loads(s)
attacks = []

for obj in data:
    a = obj['stats']['attack']
    attacks += [a]
m = sum(attacks) / len(attacks)
print(f'1: {int(m)}')
s = np.std(attacks)
print(f'2: {int(s)}')


def interval(n):
    while n >= (m - s) and n < (m + s):
        return True
    return False


names = []
for obj in data:
    for name in obj:
        a = obj['stats']['attack']
    if interval(a):
        names += [obj['name']]

print(f'3: {names}')
f.close()
