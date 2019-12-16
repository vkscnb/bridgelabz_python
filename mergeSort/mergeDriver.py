from utility.utilMethods import is_mergesort

num = int(input("enter the size of the list"))
arr=[]
while num>0:
    lst=int(input())
    arr.append(lst)
    num-=1
print(len(arr))
is_mergesort(arr,num)
