# the list "walks" is already defined
# your code here
total_distance = 0

for day_walk in walks:
    distance = day_walk["distance"]
    total_distance += distance

mean_distance = total_distance // 7
print(mean_distance)