from utility.utilMethods import is_bintodec

binval=input("enter the binary number")
binv=[]
for i in binval:
    binv.append(i)
print(binv)
is_bintodec(binv)