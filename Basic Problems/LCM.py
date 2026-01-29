def gcd(a,b):
    while b!=0:
        a, b = b, a % b
    return a

def lcm(a,b):
    return abs(a * b) // gcd(a,b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"The LCM of {num1} and {num2} is {lcm(num1, num2)}")