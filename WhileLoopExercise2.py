#Kailey Kravabloski
#10/20/2022
#In Class Exercise
#Asks the user to add to a grocery list


keepGoing = 'yes'
groceryList = []

while keepGoing == 'yes':
    item = input("Add item to grocery list: ")

    groceryList.append(item)
    print("Your List:\n", groceryList)

    keepGoing = input("Would you like to enter another item?" +
                     "(Enter yes): ")
