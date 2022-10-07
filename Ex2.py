#Kailey Kravabloski
#10/06/22
#Ex 2

itemName1 = input('Enter item 1 name: ')
itemPrice1 = float(input('Enter item 1 price: '))

itemName2 = input('Enter item 2 name: ')
itemPrice2 = float(input('Enter item 2 price: '))

itemName3 = input('Enter item 3 name: ')
itemPrice3 = float(input('Enter item 3 price: '))

itemName4 = input('Enter item 4 name: ')
itemPrice4 = float(input('Enter item 4 price: '))

itemName5 = input('Enter item 5 name: ')
itemPrice5 = float(input('Enter item 5 price: '))

total = itemPrice1 + itemPrice2 + itemPrice3 + itemPrice4 + itemPrice5

print("Your receipt:")
print(itemName1, itemPrice1)
print(itemName2, itemPrice2)
print(itemName3, itemPrice3)
print(itemName4, itemPrice4)
print(itemName5, itemPrice5)
print("Total: $", total)
