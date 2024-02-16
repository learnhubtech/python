def animal_quiz():
    score = 0

    print("Greetings! Get Ready for a Swift Quiz Session: Animals Edition!")

    # Question 1
    answer1 = input("1. What is the largest mammal in the world? ").lower()
    if answer1 == "Blue Whale" or answer1 == "blue whale":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Blue Whale.")

    # Question 2
    answer2 = input("2. Where do penguins live? ").lower()
    if answer2 == "Antarctica" or answer2 == "antarctica":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Antarctica.")

    # Question 3
    answer3 = input("3. How many legs does a spider have? ")
    if answer3 == "8":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is 8 legs.")

    # Question 4
    answer4 = input("4. What is the only mammal capable of flight? ").lower()
    if answer4 == "Bat" or answer4 == "bat":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is bat.")

    # Question 5
    answer5 = input("5. What is the natural habitat of a koala? ").lower()
    if answer5 == "Eucalyptus trees" or answer5 == "Eucalyptus forests" or answer5 == "eucalyptus trees" or answer5 == "eucalyptus forests":
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is Eucalyptus trees or forests.")

    print(f"\nQuiz completed! You scored {score} out of 5.")

if __name__ == "__main__":
    animal_quiz()
