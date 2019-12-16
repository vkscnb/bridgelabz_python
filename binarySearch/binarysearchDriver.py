from utility.utilMethods import is_binarySearch
#search for string
str=(int(input("enter the choice to binary search any number for string  or 0 for number binary search")))

if str>0:
    num = int(input("enter the size of the list in a string"))
    arr=[]
    while num>0:
        lst=input("enter the element")
        arr.append(lst)
        num-=1
    print(arr)
    search = input("enter the string element to search in the list")
    result = is_binarySearch(arr, search)
    if (result == -1):
        print("Element not present")
    else:
        print("Element found at index",result)

#search for integer
else:
    num1 = int(input("enter the size of the list in a string"))
    arr1 = []
    while num1 > 0:
        lst1 = input("enter the element")
        arr1.append(lst1)
        num1 -= 1
    intsearch = input("enter the element to search in the integer list")
    result1 = is_binarySearch((arr1,intsearch))
    print(result1)
    if (result1 == -1):
        print("Element not present")
    else:
        print("Element found at index",result1)

