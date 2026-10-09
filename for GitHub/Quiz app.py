#list and inside the list a dictionary with key:value
questions = [
    {
     "question": "What is the capital of France?",
     "options": ["Paris","London","Rome","New Delhi"],
     "answer": "Paris"
    }
]

#printing the first key of the first dictionary of the list
for i in questions:
    print(i["question"])

#printing the options key using a for loop as it's a list
    print("-----")
    for j in i["options"]:
        print(j)