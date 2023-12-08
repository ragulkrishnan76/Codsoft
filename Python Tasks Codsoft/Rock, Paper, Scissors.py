import random 
print("....Let's play Rock Paper Scissor....")
choice =['Rock','Paper','scissors']
play = 1
while(play):
 computer = random.randint(1,3)
 print("1. Rock")
 print("2. Paper")
 print("3. Scissors")
 player = int(input("Choose any number from above: "))
 print("Computer choosed: ", end="")
 if(computer == 1): print("Rock")
 elif(computer == 2): print("Paper")
 else: print("Scissor")
 if player == 1 :
   if computer == 1:
     print("Draw")
   elif computer == 2:
     print("You lose" )
   else:
     print("You win")
 elif player == 2:
   if computer == 1:
     print("You win")
   elif computer == 2:
     print("Draw")
   else:
     print("You lose")
 elif player == 3:
   if computer == 1:
     print("You lose")
   elif computer == 2:
     print("You win")
   else:
     print("Draw")
 else:
   print("Enter a valid number")
 play = int(input("\nEnter 1 to play again or 0 to stop:"))