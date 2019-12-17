#*************************************************
#@purpose :convert binary number to decimal number
#@file    :binary2decimal.py
#@author  :Vikas Sharma
#*************************************************

from utility.utilMethods import is_bintodec

binary_number=input("enter the binary number")
binary_list=[]
for binary in binary_number:
    binary_list.append(binary)
print(binary_list)
is_bintodec(binary_list)