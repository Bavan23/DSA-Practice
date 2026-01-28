grades={
    "bavan":"A",
    "ashok":"C",
    "suresh":"B",
    "ramesh":"A",
}

name=input("Enter the name of the student: ")

if name in grades:
    print(f"{name.capitalize()}'s Grade is {grades[name]}")
elif name not in grades:
    print(f"{name.capitalize()} is not in the grades.")

email=input("Enter Your Email ID: ")

if "@" in email and "." in email:
    print("Valid Email ID")
else:
    print("Invalid Email ID")