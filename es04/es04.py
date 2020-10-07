num = int(input("Gimme a number: "))

divList = []

for div in range(1, num + 1):
    if num % div == 0:
        divList.append(div)

print(divList)
