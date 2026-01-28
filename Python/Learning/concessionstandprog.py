menu={"pizza": 3.00,
      "nachos": 4.50,
      "popcorn": 6.00,
      "fries": 2.50,
      "chips": 1.00,
      "pretzel": 3.50,
      "soda": 3.00,
      "lemonade": 4.25
      }

cart=[]
total=0


print("\n------------------Menu------------------")
for keys,values in menu.items():
    print(f"{keys:10}: ${values:.2f}")
print("---------------------------------------")

while True:
    food = input("Select the food from menu or q to Quit: ").lower()
    if food.lower() == 'q':
        break
    elif food in menu:
        cart.append(food)



print("\n\n---------------Your Order---------------")
for food in cart:
    total += menu[food]
    print(f"{food:10}: ${menu[food]:.2f}")

print(f"Your Total Amount Is ${total:.2f}")

print("----------------------------------------")