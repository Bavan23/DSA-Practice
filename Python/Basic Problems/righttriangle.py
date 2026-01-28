n=int(input("Enter the Row to be printed: "))

for i in range(n+1):
    for j in range(i):
        print("* ", end="")
    print()