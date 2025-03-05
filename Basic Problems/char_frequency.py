def char_frequency(s):
    frequency = {}

    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

string= input("Enter a string: ")
frequency = char_frequency(string)

print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")