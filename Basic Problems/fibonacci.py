def print_fibonacci(n):
    a,b=0,1
    count=0

    if n<=0:
        print("Please enter a positive integer")
    elif n==1:
        print("Fibonacci series up to 1 term:")
        print(a)
    else:
        print("Fibonacci series up to",n,"terms:")

        while count<n:
            print(a,end=" ")
            next_term=a+b
            a=b
            b=next_term
            count+=1
            

num=int(input("Enter the number of terms: "))
print_fibonacci(num)