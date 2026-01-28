principle=0
time=0
rate=0

while principle<=0:
    principle=float(input("Enter the principle amount: "))
    if principle<=0:
        print("Please enter a positive number")

while rate<=0:
    rate=float(input("Enter the interest rate: "))
    if rate<=0:
        print("Please enter a positive number")

while time<=0:
    time=int(input("Enter the time in years: "))
    if principle<=0:
        print("Please enter a positive number")

total = principle* pow((1+rate/100),time)

print(f"Balance After {time} years: ${total:.2f}")