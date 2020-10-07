
import random as rm

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = rm.sample(range(1, 101), rm.randint(1, 101))
b = rm.sample(range(1, 101), rm.randint(1, 101))

x = []
for num in a:
    if num in b:
        x.append(num)

a.sort()
b.sort()
x.sort()

print(a)
print(b)
print(x)