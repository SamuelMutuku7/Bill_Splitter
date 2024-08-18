# the list "meals" is already defined
# your code here
total_calories = 0

for meal in meals:
    calories = meal["kcal"]
    total_calories += calories

print(total_calories)