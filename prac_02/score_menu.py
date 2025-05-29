def main():
    score = get_score()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print(judge_score(score))
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid option")
        print_menu()
        choice = input(">>> ").upper()
    print("Goodbye!")

def print_menu():
    print("G - Get score\nP - Print result\nS - Show stars\nQ - Quit")

def get_score():
    score = float(input("Score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid")
        score = float(input("Score (0-100): "))
    return score

def judge_score(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
