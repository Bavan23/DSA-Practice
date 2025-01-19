import  time

def stopwatch(end,start=1):
    for i in range(start,end+1):
        print(f"{i:02}")
        time.sleep(1)
    print("Time is up!!!")

stopwatch(3600)