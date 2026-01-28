import array as myarray

arr=myarray.array('i',[1,2,3,4,5])
arr2=myarray.array('u',['b','k'])
print(arr2)
print(arr)  
print(arr.typecode)

arr.insert(0,0)
for i in range(0,len(arr)):
    print(arr[i],end=' ')
print()
arr.append(6)
for i in range(0,len(arr)):
    print(arr[i],end=' ')
print()

arr[1]=0
for i in range(0,len(arr)):
    print(arr[i],end=' ')
print()

arr.pop(1)
for i in range(0,len(arr)):
    print(arr[i],end=' ')
print()

arr.remove(2) 
for i in range(0,len(arr)):
    print(arr[i],end=' ')


