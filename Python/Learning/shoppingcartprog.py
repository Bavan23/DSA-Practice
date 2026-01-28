foods=[]
prices=[]
total=0

while True:
    food=input("Enter the food item to buy or to quit press q: ")
    if food.lower()=='q':
        break
    else:
        price=float(input(f"Enter the amount of {food} $"))
        foods.append(food)
        prices.append(price)
    
for price in prices:
    total +=price

print("------------Your Cart------------")
print()
for food in foods:
    print(f"{food} ${prices[foods.index(food)]:.2f}")

print()
print(f"Total Amount of the Purchase:  {total}")