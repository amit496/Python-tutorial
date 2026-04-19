# -1 => Water
# 1 => Snake
# 0 => Gun 


import random
import time 
print("Welcome to the Snake, Water and Gun Game!")
print("Rules: ")
print("1. Snake drinks water, so snake wins.")
print("2. Gun shoots snake, so gun wins.")
print("3. Water damages gun, so water wins.")
print("4. If both players choose the same, it's a tie.")
choices = ["Snake", "Water", "Gun"]
while True:
    user_input = input("Enter your choice (Snake, Water, Gun) or 'exit' to quit: ")
    if user_input.lower() == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    if user_input not in choices:
        print("Invalid choice. Please choose Snake, Water, or Gun.")
        continue
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    if user_input == computer_choice:
        print("It's a tie!")
    elif (user_input == "Snake" and computer_choice == "Water") or (user_input == "Gun" and computer_choice == "Snake") or (user_input == "Water" and computer_choice == "Gun"):
        print("You win!")    
    else:
        print("Computer wins!")
        time.sleep(1)
    
