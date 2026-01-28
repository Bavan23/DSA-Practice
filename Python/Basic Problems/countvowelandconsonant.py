def  count_vowels_and_consonants(s):
    vowels = 'aeiouAEIOU'
    count_vowels = 0
    count_consonants = 0


    for char in s:
        if char.isalpha():
            if char in vowels:
                count_vowels += 1
            else:
                count_consonants += 1
    return count_vowels,count_consonants

string = input("Enter a string: ")
vowels, consonants = count_vowels_and_consonants(string)
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")           