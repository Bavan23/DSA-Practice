def sum_of_digits(n):
    sum_digits = 0
    while n > 0:
        digit = n % 10        # Get the last digit
        sum_digits += digit    # Add the digit to sum
        n //= 10               # Remove the last digit
    return sum_digits

num = int(input("Enter a number: "))
print(f"Sum of digits of {num} is {sum_of_digits(num)}")