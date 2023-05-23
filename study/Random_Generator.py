import random


a = set()
while len(a) < 10:
    a.add(random.randint(2, 65))
for v in a:
    print(v)
