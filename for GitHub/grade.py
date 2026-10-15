#enter the marks
grade = int(input("Enter your grade: "))

#check the grade and print the grade
#using some if-elif-else
if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")