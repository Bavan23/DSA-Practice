user = input("Whether Admin/Guest ").lower()
access="FULL ACCESS" if user=="admin" else "LIMITED ACCESS"
print(access)