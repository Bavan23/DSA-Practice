"""def find_max_min(lst):
    maximum = max(lst)
    minimum = min(lst)
    return maximum, minimum

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
maximum, minimum = find_max_min(numbers)

print(f"Maximum element: {maximum}")
print(f"Minimum element: {minimum}")"""

def find_max_min_manual(lst):
    max_val = lst[0]
    min_val = lst[0]

    for num in lst[1:]:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num

    return max_val,min_val

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
maximum, minimum = find_max_min_manual(numbers)

print(f"Maximum element: {maximum}")
print(f"Minimum element: {minimum}")