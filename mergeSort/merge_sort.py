#***********************************************
#@purpose :program for Merge sort
#@file    :merge_sort.py
#@author  :Vikas Sharma
#***********************************************

from utility.utilMethods import is_mergesort

lst_size = int(input("enter the size of the list"))
arr = []
while num>0:
    number=int(input())
    arr.append(number)
    lst_size = lst_size-1
print(len(arr))
is_mergesort(arr,lst_size)
