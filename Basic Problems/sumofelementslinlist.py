def find_sum(lst):
    total=0
    for i in lst:
        total += i
    return total
    #return sum(lst)

numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
total = find_sum(numbers)
print(f"Sum of elements: {total}")