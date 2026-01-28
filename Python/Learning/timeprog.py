import time

my_time=int(input("Enter the timer in seconds: "))

for i in range(my_time,0,-1):
    seconds=i%60
    minutes=(i//60)%60
    hours=(i//3600)
    print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    time.sleep(1)

print("Time is Up!!")