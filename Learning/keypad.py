num_pad=((1,2,3),(4,5,6),(7,8,9),('*',0,'#'))
print("\n")
for row in num_pad:
    for num in row:
        print(f"{num:>5}", end='   ')
    print("\n")

number=""
for i in range(10):
    num=input(f"Enter the Number:")
    number +=num

print(f"Dialling {number}")
'''
def display_keypad():
    """Display the keypad layout."""
    num_pad = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ('*', 0, '#'))
    print("\nKeypad:")
    for row in num_pad:
        for num in row:
            print(f"{num:>5}", end='   ')
        print("\n")

def get_number():
    """Collect numbers from the user."""
    number = ""
    while True:
        num = input("Enter the Number (Press # to finish): ")
        if num == "#":
            break
        if num not in "0123456789*#":
            print("Invalid input. Try again.")
            continue
        number += num
        print(f"Current number: {number}")
    return number

# Main Program
display_keypad()
dialed_number = get_number()
print(f"Dialling {dialed_number}")'''
