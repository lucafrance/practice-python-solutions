a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

check = int(input("What's the maximum? "))

for number in a:
    if number < check:
        b.append(number)

print(b)