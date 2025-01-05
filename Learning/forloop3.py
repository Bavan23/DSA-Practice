odd=0
even=0
a=int(input())
b=int(input())
for i in range(a,b):
    if(i%2==0):
        even=even+1
    else:
        odd=odd+1
print(even)
print(odd)
