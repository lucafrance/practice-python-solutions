def divisors_list(num):
    div_list = []
    for div in range(1, num + 1):
        if num % div == 0:
            div_list.append(div)
    return div_list


prime_numbers = [1]
for num in range(2, 10000):
    if divisors_list(num) == [1, num]:
        prime_numbers.append(num)

print(prime_numbers)
