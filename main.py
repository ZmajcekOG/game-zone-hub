import random
import time

def print_banner():
    print("=" * 45)
    print("   WELCOME TO THE INTERACTIVE GAME ZONE HUB   ")
    print("=" * 45)

def number_guessing_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    print("\n[Game] Guess the secret number between 1 and 100!")
    
    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed {secret_number} in {attempts} attempts!")
                break
        except ValueError:
            print("Please enter a valid integer.")

def player_card_generator():
    names = ["Alex", "Jordan", "Sam", "Chris"]
    roles = ["Striker", "Midfielder", "Defender", "Playmaker"]
    
    print("\n[Generator] Generating random player profile...")
    time.sleep(1)
    
    player_name = random.choice(names)
    player_role = random.choice(roles)
    rating = random.randint(82, 99)
    
    print(f"⭐ Player: {player_name} | Role: {player_role} | Rating: {rating}/99")

if __name__ == "__main__":
    print_banner()
    player_card_generator()
    number_guessing_game()
