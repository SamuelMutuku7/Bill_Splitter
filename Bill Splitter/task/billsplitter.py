import random

# Get the number of people attending the dinner from the user and initialize an empty names dictionary
user_input = int(input("Enter the number of friends joining (including you): "))

# Reject the input in the event it suggests no one will be attending
if user_input < 1:
    print("No one is joining for the party")
else:
    # Get the names of the friends
    print("Enter the name of every friend (including you), each on a new line:")
    names = {}
    for _ in range(user_input):
        name = input()
        names[name] = 0  # Initialize each friend's contribution to 0

    # Get the total bill amount
    total_bill = float(input("Enter the total bill value: "))

    # Calculate the bill per person without using the "Who is lucky?" feature
    individual_bill = round(total_bill / user_input, 2)
    for name in names:
        names[name] = individual_bill

    # Ask if the user wants to use the "Who is lucky?" feature
    who_is_lucky = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')

    if who_is_lucky == "Yes":
        lucky_name = random.choice(list(names.keys()))
        print(f"{lucky_name} is the lucky one!")

        # Recalculate the bill for everyone except the lucky one
        individual_bill = round(total_bill / (user_input - 1), 2)
        for name in names:
            if name == lucky_name:
                names[name] = 0
            else:
                names[name] = individual_bill

        print(names)

    else:
        print("No one is going to be lucky")
        print(names)