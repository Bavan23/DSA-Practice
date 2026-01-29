def remove_duplicate(lst):
    #return list(set(lst))
    # 
    return list(dict.fromkeys(lst))
"""
    unique=[]
    for num in lst:
        if num not in unique:
            unique.append(num)
    return unique"""

   


lst=[int(x) for x in input().split()]
print(remove_duplicate(lst))