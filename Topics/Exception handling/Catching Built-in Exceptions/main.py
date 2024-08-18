a = int(input())
b = int(input())

try:
    dividend = a / b
except ZeroDivisionError:
    print("The Error!")
else:
    print(dividend)