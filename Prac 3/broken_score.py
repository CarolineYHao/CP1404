def main():
    score = float(input("Enter score: "))
    result_text = process_result(score)
    print(result_text)


def process_result(score):
    if score < 0 or score > 100:
        result_text = "Invalid score"
    elif score >= 90:
        result_text = "Excellent"
    elif score >= 50:
        result_text = "Passable"
    else:
        result_text = "Bad"
    return result_text


main()
