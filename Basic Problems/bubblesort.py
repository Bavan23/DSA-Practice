def bubble_sort(arr):
    n=len(arr)
    #   return sorted(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

lst=[int(x) for x in input("Enter the numbers: ").split()]
print(bubble_sort(lst))  # This will print None because the function is not implemented