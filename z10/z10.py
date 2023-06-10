num = int(input('введите количество монет на столе: '))
import random


o = 0
r = 0
for i in range(num):
    moneta = random.choice([True, False])
    if moneta == True:
        o += 1
    else:
        r += 1
if o <= r:
    print(f'минимальное количество монет {o}')
else:
    print(f'минимальное количество монет {r}')
