import random
userInput = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

computerInput = random.randint(0, 2)
computer_score=0
user_score=0

if userInput == computerInput:
    print("Draw")
elif (userInput == 0 and computerInput == 2) or (userInput == 1 and computerInput == 0) or (userInput == 2 and computerInput == 1):
    print("You Win!")
    user_score +=1
else:
    print("Computer Wins!")
    computer_score +=1

if computerInput == 0:
    print("Computer choice: Rock")
elif computerInput == 1:
    print("Computer choice: Paper")
elif computerInput == 2:
    print("Computer choice: Scissors")
    

print("The score of Computer is" , computer_score)
print("The score of User is" , user_score)
