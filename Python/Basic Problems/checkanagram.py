def are_anagrams(s1, s2):
    s1=s1.replace(" ","").lower()
    s2=s2.replace(" ","").lower()

    return sorted(s1) == sorted(s2)

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")