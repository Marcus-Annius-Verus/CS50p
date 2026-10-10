#create a def for a 10s thinking timer
import time
import json

def timer():
    secs = 10
    while secs > 0:
        print(f"{secs:02d}", end='\r')
        time.sleep(1)
        secs -= 1
    return print("Time's up!, choose answer.")

#list and inside the list a dictionary with key:value
questions = [
    {
     "question": "What is the capital of France?",
     "options": ["Paris","London","Rome","New Delhi"],
     "answer": "Paris"
    },

    {
    "question": "Where was Julius Caesar born?",
    "options": ["Jerusalem","Bohemia","Rome","Gotham"],
    "answer": "Rome"
    },

    {
        "question": "How tall is Mt.Everest?",
        "options": ["8848m","8850m","12000m","9000m"],
        "answer": "8850m"
    },

    {
        "question": "Who founded Apple?",
        "options": ["Steve","Jobs","Steve Jobs","Batman"],
        "answer": "Steve Jobs"
    },

    {
        "question": "Who was Akbar?",
        "options": ["Indian King","Dancer","Serial Killer","Gamer"],
        "answer": "Indian King"
    }
]
#storing the value 0 as a which can increase at the end of the loop to keep the answer looping
#and not get stuck on the answer of the first dictionary
a = 0

#storing the question number as 1 which will also increment with the loop.
question_num = 1

#same for storing no. of correct and incorrect answers
correct_num = 0
incorrect_num = 0

#printing the first key of the first dictionary of the list
for i in questions:
    print(f"Question: {question_num:02d}")
    print(i["question"])

    #printing the options key using a for loop as it's a list for value
    print("-----")
    for j in i["options"]:
        print(j)

    #accept the user input beyond this point with checking for right answer
    print("-----")

    #giving 10s to think before choosing answer
    timer()

    choice = input("Enter your answer: ")
    correct = questions[a]["answer"]

    print("-----")

    if choice.lower() == correct.lower():
        print("Yes, that is the answer!")
        correct_num += 1
    else:
        print("Sorry, that's incorrect.")
        incorrect_num += 1

    a += 1
    question_num += 1
    print("-----")

print(f"Correct answers: {correct_num}")
print(f"Incorrect answers: {incorrect_num}")
print("Thank you for playing!")