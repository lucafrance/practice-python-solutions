import webbrowser

def fibonacci_sequence(num):
    if num <= 0:
        return []
    if num == 1:
        return [1]

    fib = [1, 1]
    num = num - 2
    while num:
        fib.append(fib[-1] + fib[-2])
        num -= 1
    return fib


num = int(input("How many Fibonacci numbers do you want? "))

file_name = "Fibonacci sequence.txt"
file = open(file_name, "w")
for x in fibonacci_sequence(num):
    file.write(str(x) + "\n")
file.close()

webbrowser.open(file_name)

