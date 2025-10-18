import random


def generate_number(difficulty):
    return random.randint(1, difficulty)

def get_guess_from_user():
    difficulty = int(input("Enter the difficulty level: "))
    guess = int(input(f"Guess a number between 1 and {difficulty}: "))
    return difficulty, guess

def compare_results(secret_number, guess) -> bool:
    return secret_number == guess

def play():
    difficulty, guess = get_guess_from_user()
    secret_number = generate_number(difficulty)
    if compare_results(secret_number, guess):
        print("You won!")
    else:
        print("You lost!")
        

if __name__ == "__main__":
    play()


