from utility.utilMethods import is_insertion

num = int(input("enter the size of the list"))
name=[]

while num>=0:
    print("enter the name in the list")
    sname=input()
    name.append(sname)
    num-=1
print(name)
print()
name2=is_insertion(name)
print(name2)