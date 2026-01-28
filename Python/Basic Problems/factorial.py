def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers."
    elif n == 0 or n == 1:
        return 1    
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")