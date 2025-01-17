#simple quiz game in python
#author: @bavan23
import time

questions=("How Many Elements Are there in Periodic Table?: ",
           "Which Animal Lays Largest Egg?: ",
           "What is the most abundant gas oon the Earth's Attmmosphere?: ",
           "How many bones are there in Human Body?: ",
           "WHich planet in the solar sysem is Hottes?: ")

options=(("A. 116","B. 117","C. 118","D. 119"),
         ("A. Lion","B. Crocodile","C. Ostrich","D. Elephant"),
         ("A. Nitrogen","B. Oxygen","C. Carbon-dioxide","D. Hydrogen"),
         ("A. 112","B. 209","C. 207","D. 206"),
         ("A. Merucury","B. Venus ","C. Earth","D. Mars"))

answers=("C","C","A","D","B")

guesses=[]
score=0
question_num=0   

for qn in questions:
    print("--------------------------------")
    print(qn)

    for j in options[question_num]:
        print(j)
    print()
    guess=input("Enter the Correct Option: ").upper()
    guesses.append(guess)
    print()
    if guess == answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT! The correct answer is",answers[question_num])

    question_num+=1
    time.sleep(1)
    print("\n")
print("\n")

print("---------------------------")
print("           Result          ")
print("---------------------------")

print(f"You Have Answered {score} out of 5!!")