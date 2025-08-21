import random
user_choice=int(input("Enter your choice: Type 0 for Rock , 1 for Paper , 2 for Scissors."))

if user_choice >=3 or user_choice<0:
 print("invalid input:You Lose")

else:
 computer_choice=random.randint(0,2)
 print("Computer choose:")
 print(computer_choice)
 if computer_choice == user_choice:
     print("It is draw.")
 elif computer_choice==0 and user_choice==2:
     print("You lose.")
 elif computer_choice==2 and user_choice==0:
     print("You win.")
 elif computer_choice>user_choice:
      print("You lose.")
 elif computer_choice<user_choice:
     print("You win.")
    