
prime_numbers = [int(n) for n in open("primenumbers.txt", "rt").read().splitlines(False)]
happy_numbers = [int(n) for n in open("happynumbers.txt", "rt").read().splitlines(False)]

prime_and_happy_numbers = []
for n in prime_numbers + happy_numbers:
    if n in prime_numbers and n in happy_numbers:
        prime_and_happy_numbers.append(n)

print(prime_and_happy_numbers)
