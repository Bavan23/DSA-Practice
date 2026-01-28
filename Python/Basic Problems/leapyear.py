def is_leapYear(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


is_leapYear(int(input("Enter the Year to check: ")))