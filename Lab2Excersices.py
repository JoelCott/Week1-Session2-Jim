itemPrice = float(input("Enter the item price: "))
itemQuantity = int(input("Enter the quantity of product(s): "))
itemTax = itemPrice * 20 / 100 + itemPrice
itemFinalTax = itemTax * itemQuantity
totalPrice = itemPrice + itemFinalTax
print("Tax on the item(s) is", itemFinalTax)
print("Total item price is", totalPrice)

year = int(input("Enter the year you were born: "))
if year % 4 == 0:
    print("You were born in a leap year")
    #year = str(year)

elif year == 2006:
    print("You were born in the same year as me!")
else:
    print("You was not born in a leap year")

age = int(input("How old are you?: "))

if age > 18:
    print("You are older than me!")
elif age < 18:
    print("You are younger than me!")
else:
    print("You are the same age as me!")

myName = "John"