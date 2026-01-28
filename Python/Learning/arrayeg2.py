import array as myarray

ar=list(range(0,51,2))
arr=myarray.array('i',ar)


so=arr.tolist()
so.sort(reverse=True)
print(so)