print("Prime numbers between 1 and 100 are:")
prime=[]
for num in range(1, 101):
    if num > 1:  # prime numbers are greater than 1
        is_prime = True
        for i in range(2, int(num**0.5) + 1):  # check divisibility up to √num
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(num)
print(prime)