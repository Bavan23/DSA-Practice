def remove_duplicates(s):
    #return ''.join(sorted(set(s)))
    #return ''.join(sorted(set(s), key=s.index)))  # use index as key to preserv
    result=''
    seen=set()

    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    return result

string = input("Enter a string: ")
no_duplicates = remove_duplicates(string)
print(f"String after removing duplicates: {no_duplicates}")