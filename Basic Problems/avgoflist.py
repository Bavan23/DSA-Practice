def average(lst):
    if len(lst) == 0:
        return "List is empty, cannot calculate average."
    return sum(lst) / len(lst)

lst=[int(x) for x in input().split()]
print(f"The average of the list is :{average(lst)}")