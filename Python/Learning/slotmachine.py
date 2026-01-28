# Python Slot Machine

import random

def spin_out():
    symbols=["🍒", "🍉" ,"🍋" ,"🔔", "⭐"]
    results=[random.choice(symbols) for _ in range(3)]
    return results

def print_row(row):
    #for i in row:
    #   print(i,end=" ")
    # or 
    print("************")
    print(" | ".join(row))
    print("************")

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]=="🍒":
            return bet*2
        elif row[0]=="🍉":
            return bet*3
        elif row[0]=="🍋":
            return bet*5
        
        elif row[0]=="🔔":
            return bet*10
        elif row[0]=='⭐':
            return bet*20
    else:
        return 0

def main():
    balance=100

    print("\n\n******************************")
    print(" Welcome to Slot Machine Game ")
    print("   Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("******************************")

    while balance>0:
        print(f"\nCurrent Balance: ${balance}")
        
        bet = input("\nEnter Your Bet Amount:  ")

        if not bet.isdigit():
            print("\nInvalid Input. Please enter a number.")
            continue
        bet = int(bet)

        if bet>balance:
            print("\nInsufficient Balance. Please enter a valid bet amount. ")
            continue

        if bet<=0:
            print("\nInvalid Bet Amount. Please enter a positive number.")
            continue
        

        balance-=bet
        
        row=spin_out()
        
        print("\nSpinning.....\n")
        print_row(row)
         
        payout=get_payout(row,bet)
        
        if payout>0:
            print(f"\nYayy!! You Won ${payout}!")
        else:
            print("\nBetter Luck Next Time!")
         
        balance+=payout

        play_again=input("Do You Wanna Play Again?? (Y/N): ").upper()

        if play_again != 'Y':
            break

    print("\n\n***********************************************")
    print(f" Game Over!! Your Final Balance is ${balance}")
    print("***********************************************")

if __name__=='__main__':
    main()