guests = []
capacity = 0

while True:
    person = input()
    if person == ".":
        break
    guests.append(person)
    capacity += 1

print(guests)
print(capacity)