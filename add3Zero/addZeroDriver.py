#***********************************************
#@purpose :combination of three digit is zero
#@file    :add3Zero.py
#@author  :Vikas Sharma
#***********************************************
from utility.utilMethods import is_add

size = int(input("enter the size of the list"))
lst=[]
for i in range(size):
    lst.append(int(input()))
is_add(lst,size)

