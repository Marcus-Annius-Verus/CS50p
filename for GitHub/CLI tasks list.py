import json

#accessing the data from the json file during execution
with open("tasks.json","r") as file:
    task_list = json.load(file)

#Empty task list and options to choose from?
print("1 to add tasks.")
print("2 to remove tasks.")
print("3 to display tasks.")
print("4 to display choice list again.")
print("5 to exit.")

#creating an infinite loop to do everything until user enters "5"
while True:
    choice = int(input("Enter choice (1,2,3,4,5): "))

    if choice == 1:
        add_task = input("Enter task? ")
        task_list.append(add_task)
    
    elif choice == 2:
        remove_task = input("Which task? ")
        task_list.remove(remove_task)
    
    elif choice == 3:
        for t in task_list:
            print(t)
    
    elif choice == 4:
        print("1 to add tasks.")
        print("2 to remove tasks.")
        print("3 to display tasks.")
        print("4 to display choice list again.")
        print("5 to exit.")

    elif choice == 5:
        print("Have a nice day!")
        break

    else:
        print("enter only numbers!")

#storing data in the json file at the end 
with open("tasks.json","w") as json_file:
    json.dump(task_list, json_file, indent=4)