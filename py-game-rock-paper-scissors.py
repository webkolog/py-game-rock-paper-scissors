import random
items = ["rock", "paper", "scissor"]
computer = random.choice(items)
user = input("rock, paper, or scissor:").lower().strip()
print("Computer choose:",computer)
if user not in items:
    print("invalid choice! Please choose rock, paper, or scissor.")
elif user == computer:
    print("Match draw!")
elif user == "rock" and computer == "scissor" or user == "paper" and computer == "rock" or user == "scissor" and computer == "paper":
    print("User win!")
else:
    print("Computer win!")