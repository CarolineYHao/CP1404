def main():
    score = float(input("Enter score: "))
    result_text = process_result(score)
    print(result_text)


def process_result(score):
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    if score > 90:
        result_text = "Excellent"
    else:
        if score >= 50:
            result_text = "Passable"
        elif score < 50:
            result_text = "Bad"
    return result_text


main()
