#!/usr/bin/python
import random

def predict_winner(user_choice, computer_choice):
    # Rules for determining the winner
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "you win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to the game named ROCK, PAPER, SCISSORS!")
    print("Choices: rock, paper, scissors")
    
    # User input
    name=input("please tell us your name")
    user_choice = input("  Enter your choice: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return
    
    # Computer's random choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    
    # Predict and display the winner
    result = predict_winner(user_choice, computer_choice)
    print(result)

# Run the game
play_game()
