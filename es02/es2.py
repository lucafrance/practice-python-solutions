num = int(input("What's the number to check? "))
check = int(input("What's the number to divide by? "))
if num % 4 == 0:
    print("It's a multiple of 4! :)")
elif num % check == 0:
    print(str(num) + " is divisible by " + str(check))
else:
    print(str(num) + " ain't divisible by " + str(check))