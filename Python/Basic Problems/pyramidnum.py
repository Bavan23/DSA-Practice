n = int(input("Enter the number of rows: "))

for i in range(1, n + 1):
    # Print leading spaces
    for j in range(n - i):
        print(" ", end=" ")

    # Print increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")

    # Print decreasing numbers
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()  # Move to next line after each row
