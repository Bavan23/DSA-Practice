groceries=[["Apple","Oranges","Pineapple"],["Carrot","raddish","beetroot"],["Chicken","Mutton","Salmon"]]

print(groceries)

for i in groceries:
    for items in i:
        print(items,end=" ")
    print()

groceries[0][0]="apple"
print(groceries)
