def reverse(n):
    reverse_num=0
    while n>0:
        remainder=n%10
        reverse_num=reverse_num*10+remainder
        n=n//10
    return reverse_num

num = int(input("Enter a number: "))
print(f"Reversed number is {reverse(num)}")