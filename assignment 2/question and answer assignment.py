# creating a list of questions
questions = [
    ("What is the fastest land animal?", "cheetah", "medium", 2),
    ("What is the chemical symbol of Gold?", "au", "hard", 3),
    ("The year World War II ended?", "1945", "hard", 3),
    ("How many local governments are in Abia State?", "17", "easy", 1),
    ("What is the largest ocean?", "pacific ocean", "easy", 1),
    ("Who created Python?", "guido", "hard", 3),
    ("Who was the first man to travel to moon?", "armstrong", "hard", 3),
    ("Who is the President of Nigeria?", "bola ahmed tinubu", "easy", 1),
    ("What is the largest desert?", "sahara desert", "medium", 2),
    ("Who is the VC of LearnFactory?", "mr. chibueze ikedi", "easy", 1),
    ("What is the most populated country in Africa?", "nigeria", "easy", 1),
    ("How many states are in Nigeria?", "36", "easy", 1),
    ("What is the square root of 36?", "6", "medium", 2),
    ("What is the approximate speed of light in km/s?", "300000", "hard", 3),
    ("Who is the richest man in the world?", "elon musk", "medium", 2)
]


# function to run the quiz
def run_quiz(level):
    score = 0
    total_points = 0

    # loop through questions
    for question, answer, difficulty, points in questions:

        if difficulty == level:
            print(question)
            user_answer = input("Your answer: ").lower()

            if user_answer == answer:
                print("Correct!\n")
                score += points
            else:
                print("Wrong! Correct answer is:", answer, "\n")

            total_points += points

    # calculate percentage
    percent = (score / total_points) * 100

    print("You scored", score, "out of", total_points)
    print("Percentage:", round(percent, 1), "%")

    # performance message
    if percent == 100:
        print("Excellent! Perfect score!")
    elif percent >= 70:
        print("Great job, you did well!")
    elif percent >= 40:
        print("Not bad, but you can improve.")
    else:
        print("Keep practicing, don’t give up!")


# Example run
run_quiz("easy")