try:
    a=int(input())
    b=int(input())
    c=input()
    if c=="+":
        print(a+b)


except ValueError as e:
    print("Error Because -",e)

except TypeError as e:
    print("Error Because -",e)

except NameError as e:
    print("Error Because -",e) 

except Exception as e:
    print("Error Because -",e)

finally:
    print("This is finally block, Thus Code has been completed!")