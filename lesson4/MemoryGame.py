import random, time

def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    return [int(input(f"Enter the number {i+1}: ")) for i in range(difficulty)]

def is_list_equal(list1, list2):        
    return list1 == list2

def play(difficulty):   
    sequence = generate_sequence(difficulty)
    print(sequence)
    time.sleep(0.7)
    print("\n" * 30)
    user_list = get_list_from_user(difficulty)
    return is_list_equal(sequence, user_list)


if __name__ == "__main__":
    difficulty = int(input("Enter the difficulty level: "))
    if play(difficulty):
        print("You won!")
    else:
        print("You lost!")