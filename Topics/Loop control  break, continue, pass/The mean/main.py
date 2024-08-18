total = 0
count = 0

while True:
    number = input()
    if number == ".":
        break
    total += int(number)
    count += 1

average = total / count
print(average)
