import random

a = [random.randint(0, 10) for i in range(0, 10)]
b = sorted(a)
b.insert(0, 1)
b.insert(1, 2)
b.insert(2, 3)
print(b)

