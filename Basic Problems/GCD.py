def find_gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd=find_gcd(num1,num2)
print("The GCD of",num1,"and",num2,"is",gcd)