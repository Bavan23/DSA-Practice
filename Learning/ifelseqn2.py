name=input("Enter your name-")
income=int(input("Enter your income-"))
age=int(input("Enter your age-"))

if(income>=25000 or age>=20):
    loan=int(input("Enter  your loan amount-"))
    if(loan>50000):
        print(name,"Loan shouldnt exceed 50000")
    else:
        print(name,"You are eligible For loan")
else:
    print(name,"You are not elidible for loan:")
