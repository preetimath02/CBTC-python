import random

def print_options():
    print("\nChoices:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors\n")

def get_user_choice():
    choice = input("Enter your choice (1, 2, or 3): ")
    while choice not in ["1", "2", "3"]:
        print("Unsupported choice. Please try again.\n")
        print_options()
        choice = input("Enter your choice (1, 2, or 3): ")
    return choice

def get_computer_choice():
    return str(random.randint(1, 3))

def print_round_result(user_choice, comp_choice, user_score, comp_score):
    choices_mapping = {"1": "Rock", "2": "Paper", "3": "Scissors"}
    user_choice_str = choices_mapping[user_choice]
    comp_choice_str = choices_mapping[comp_choice]

    print(f"Human pick-out {user_choice_str}")
    print(f"Computer pick-out {comp_choice_str}")

    if user_choice == comp_choice:
        print("It's a draw!")
    elif (user_choice == "1" and comp_choice == "3") or \
        (user_choice == "2" and comp_choice == "1") or \
        (user_choice == "3" and comp_choice == "2"):
        print("Homo-Sapiens win this round!")
        user_score += 1
    else:
        print("Artificial mind wins this round!")
        comp_score += 1

    print(f"Score: You {user_score}, Computer {comp_score}\n")

def print_final_result(user_score, comp_score):
    if user_score > comp_score:
        print("Yay...Congratulations!!! You win!!")
    elif user_score < comp_score:
        print("Sorry,our artificial mind wins. Hope you do well next time.")
    else:
        print("It's a draw match!")


print("⚝──⭒─⭑─⭒──⚝ 𝐑𝐨 -- 𝐬𝐡𝐚𝐦 -- 𝐛𝐨 ⚝──⭒─⭑─⭒──⚝\n")

rounds = int(input("How many rounds you wish? "))
print_options()

user_score = 0
comp_score = 0

for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}:")
    user_choice = get_user_choice()
    comp_choice = get_computer_choice()
    print_round_result(user_choice, comp_choice, user_score, comp_score)

print_final_result(user_score, comp_score)