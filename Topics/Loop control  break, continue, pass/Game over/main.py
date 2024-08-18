scores = input().split()
# put your python code here
correct_answers = 0
incorrect_answers = 0

for i in range(len(scores)):
    current_answer = scores[i]

    if current_answer == "C":
        correct_answers += 1
    elif current_answer == "I":
        incorrect_answers += 1

    if incorrect_answers == 3:
        print(f"Game over\n{correct_answers}")
        break
else:
    print(f"You won\n{correct_answers}")
