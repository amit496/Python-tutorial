import random
import time

choice = ["Water", "Snake", "Gun"]

while True:
    user_input = input("Enter your choice (Water, Snake, Gun) or 'exit' to quit: ").capitalize()
    
    if user_input == 'Exit':
        print("Thanks for playing! Goodbye!")
        break
    elif user_input not in choice:
        print("Invalid choice. Please choose Water, Snake, or Gun.")
        continue
    
    computer_choice = random.choice(choice)
    print("Computer is choosing...")
    time.sleep(1)
    print(f"Computer chose: {computer_choice}")
    
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "Water" and computer_choice == "Gun") or (user_input == "Snake" and computer_choice == "Water") or (user_input == "Gun" and computer_choice == "Snake"):
        print("You win!")
    else:
        print("Computer wins!")

