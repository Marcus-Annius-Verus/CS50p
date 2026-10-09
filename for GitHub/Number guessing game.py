#importing random to generate the number
import random

#generating the random number and prompting user and storing tries
a = int(input("Enter the upper range: "))
b = int(input("Enter the lower range: "))
random_num = random.randint(a,b)
print(random_num)
print("Enter your guess or exit")
count = 0

#infinite loop to guess the number until exit
while True:
    guess = input("guess? ")

#try and catch block for when exit is entered
    try:
        if int(guess) > random_num:
            print("Too high!")
            count += 1

        elif int(guess) < random_num:
            print("Too low!")
            count += 1

        elif int(guess) == random_num:
            print("Congratulations!")
            print(f"Tries: {count}")
            break
    
    except ValueError:
        if guess == "exit":
            print(f"The number was {random_num}")
            print(f"Tries: {count}")
            print("bye.")
            break




