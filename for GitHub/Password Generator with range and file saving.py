#importing modules
import random
import string

#entering length from the user of the password
print("-------------")
pass_len = int(input("How long do you want your password? "))

#taking choice of yes and no for what to include and storing them in their respective variables
print("-------------")
letter_bool = input("include letters? (yes/no) ")
number_bool = input("include digits? (yes/no) ")
sign_bool = input("include signs? (yes/no) ")

#adding the chars to the main character set from which the password will be generated
#adding exit if all are "no"
final_chars = ""
if letter_bool == "yes":
    final_chars += string.ascii_letters
if number_bool == "yes":
    final_chars += string.digits
if sign_bool == "yes":
    final_chars += string.punctuation
if letter_bool == number_bool == sign_bool == "no":
    print("Password cannot be empty!")
    exit()


#making a final list for the password
#running the loop till length and adding the values to the list
password = []
for i in range(pass_len):
    pass1 = random.choice(final_chars)
    password.append(pass1)

print("-------------")
#printing the final list with .join and in one sequence
print("Your password: "+"".join(password))

print("-------------")
#asking saving permission
#and converting password to a string as the write needs to be an str file and not a list
save = input("Do you wish to save the password to a file(yes/no)? ")
str_pass = "".join(password)

#make the file which will store the password safely with user permission and print confirmation 
#when done or just print a thank you
if save == "yes":
    with open("password file.txt","w") as pass_file:
        pass_file.write(str_pass)
    print("Password saved.")
    print("Thanks and have a nice day.")
else:
    print("Thanks and have a nice day.")







