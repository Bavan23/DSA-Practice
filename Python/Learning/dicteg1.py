grades={"bab":2,"alic":3,"ram":2}

name=input()

if name in grades:
    print(f"Grade of {name} is {grades[name]}")
else:
    print(f"No grade found for {name}")
