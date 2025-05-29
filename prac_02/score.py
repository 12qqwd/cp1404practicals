def get_score():
    score = input("Enter score: ")
    try:
        score = float(score)
        return score
    except:
        print("Invalid input")
        return None

def check_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    score = get_score()
    if score is not None:
        result = check_score(score)
        print(result)

main()

