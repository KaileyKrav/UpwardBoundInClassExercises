#Kailey Kravabloski
#10/20/2022
#In Class Example
#Asks the user to input grades for a student


keepGoing = 'y'

while keepGoing == 'y':
    grade = int(input("Please enter a grade: "))
    
    if grade >= 90:
        print(grade, 'A')
    elif grade >= 80:
        print(grade, 'B')
    elif grade >= 70:
        print(grade, 'C')
    else:
        print(grade, 'F')

    keepGoing = input('Would you like to enter another grade?' +
                      '(Enter y for yes): ')
