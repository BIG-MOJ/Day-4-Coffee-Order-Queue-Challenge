totalPrice = 0
drinkCount = 0
while True:
    name = input("Please enter your name (or 'done' to finish): ")
    if name == "done":
        break
    drink = input("Enter order for "+ name + ": ")
    if drink == "latte":
        totalPrice += 3.50
        drinkCount += 1
    elif drink == "americano":
        totalPrice += 3.00
        drinkCount += 1
    elif drink == "espresso":
        totalPrice += 2.50
        drinkCount += 1
    else:
        print(f"Warning!!! {drink} not recognized")
        continue
print("Order Queue Completed")
print(f"Total drink ordered: {drinkCount} drinks")
print(f"Total price: $ {totalPrice}")