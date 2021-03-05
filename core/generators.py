# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100

import random

def gen(N):
    for _ in range(N):
        yield random.randint(1, 100)

# написать генераторное выражение, которое делает то же самое

gen2 = lambda N: (random.randint(1, 100) for _ in range(N))