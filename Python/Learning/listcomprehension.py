list=[str(x) for x in range(1,11) if x>0]
print(list)

grades=[70,60,40,30,90,91,69]

passed_students=[stu for stu in grades if stu>=60]
print(passed_students)

twodtuple=((1,2,3),(7,8,9),(4,5,6))

ans=[j for i in twodtuple for j in i if j>3]  
print(ans)