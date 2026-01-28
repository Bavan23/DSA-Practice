def second_largest(lst):
    if len(lst)<0:
        return "List must have at least two distinct elements"
    
    first=second=float('-inf')

    for num in lst:
        if num>first:
            second=first
            first=num
        elif num>second and num!=first:
            second=num

    if second == float('-inf'):
        return "There is no second largest element (all elements might be the same)"
    
    return second

nums = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("Second largest element:", second_largest(nums))