def show_balance(balance):
    print(f"\nYour Balance is ${balance:.2f}\n")
    

def deposit():
    amount=float(input("\nEnter the Amount to be deposited:  "))
    if amount<0:
        print("\nInvalid Amount. Please enter a positive number.")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("\nEnter the Amount to be withdrawn:  "))
    if amount > balance:
        print("\nInsufficient Balance. Please enter a smaller amount.")
        return 0
    elif amount<0:
        print("\nInvalid Amount. Please enter a positive number.")
        return 0
    else:
        return amount


def main():

    balance=0
    is_running = True

    while is_running:
        print("\nBanking Program!!\n")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice=input("\nEnter your Choice: ")

        match choice:
            case "1":
                show_balance(balance)
            case "2":
                balance += deposit()
            case "3":
                balance-=withdraw(balance)
            case "4":
                is_running = False
            case _:
                print("\nInvalid Choice!! Please try again!!\n")

    print("\nThankyou!! Have a Nice Day!!")

if __name__=='__main__':
    main()