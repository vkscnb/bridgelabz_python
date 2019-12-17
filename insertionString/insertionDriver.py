#***********************************************
#@purpose :program for Insertion sort
#@file    :insertion_sort.py
#@author  :Vikas Sharma
#***********************************************

from utility.utilMethods import is_insertion

lst_size = int(input("enter the size of the list"))
name = []

while lst_size >= 0:
    print("enter the name in the list")
    sname = input()
    name.append(sname)
    num = num -1
print(name)
print()
name2 = is_insertion(name)
print(name2)