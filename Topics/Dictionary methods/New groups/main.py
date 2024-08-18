# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
number_of_groups = int(input())  # Number of groups to be filled
class_size = {}  # Initialize an empty dictionary

for i in range(len(groups)):  # Iterate over all groups
    if i < number_of_groups:  # If within the number of groups to be filled
        number_of_children = int(input())  # Input for number of children in the group
        class_size[groups[i]] = number_of_children  # Assign the number of children to the group
    else:
        class_size[groups[i]] = None  # Assign None to unfilled groups

print(class_size)
