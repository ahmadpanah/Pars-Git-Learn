quiz = {
    "question1" : {
        "question": "What is Captial of Iran?",
        "answer": "Tehran"
    },
    "question2" : {
        "question": "What is Captial of France?",
        "answer": "Paris"
    },
    "question3" : {
        "question": "What is Captial of Turkey?",
        "answer": "Ankara"
    },
}

score = 0

for key,value in quiz.items():
    print (value['question'])
    answer = input("Answer?")

    if answer.lower() == value['answer'].lower():
        print("Correct! 👌")
        score = score + 1
        print ("Your Score is: " + str(score))

    else:
        print("Wrong!")
        print ("The Answer is: " + value['answer'])
        print ("Your Score is: " + str(score))