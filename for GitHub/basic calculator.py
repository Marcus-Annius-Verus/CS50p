#ask the user for input of 2 numbers and the operator
num1 = float(input("Enter the first number? "))
num2 = float(input("Enter the second number? "))
oper = input("Choose operator (+,-,*,/)? ")

#perform the operation based on the choice
if oper == "+":
    print(num1+num2)
elif oper == "-":
    print(num1-num2)
elif oper == "*":
    print(num1*num2)
elif oper == "/":
    print(num1/num2)
else:
    print("Please enter a valid character!")
