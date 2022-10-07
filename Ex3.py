#Kailey Kravabloski
#10/06
#In Class Exercise 3
#This program asks the user for their score
#and outputs the corresponding letter grade

score = int(input("Please enter your score: "))

if score >= 90:
    print('Your grade is A')
elif score >= 80:
    print('Your grade is B')
elif score >= 70:
    print('Your grade is C')
else:
    print('Your grade is F')
