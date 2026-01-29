import threading
import time

def stand():
    time.sleep(2)
    print("I'm standing")
    

def walk():
    time.sleep(4)
    print("I'm walking")
   

def say(smtg):
    time.sleep(1)
    print(smtg)

chore1=threading.Thread(target=stand)
chore2=threading.Thread(target=walk)
chore3=threading.Thread(target=say,args=("Hello",))
chore1.start()
chore2.start()
chore3.start()

chore1.join()
chore2.join()
chore3.join()
print("hel")