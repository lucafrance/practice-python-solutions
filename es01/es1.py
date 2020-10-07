
age = int(input("How old are ya?"))
printCount = int(input("How many times do you want to see the message?"))
message = "You will be 100 years old in the year " + str(2020 + 100 -age)

while printCount > 0:
    print(message)
    printCount -= 1


