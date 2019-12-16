#***********************************************
#@purpose :check parenthesis is equal or not
#@file    :parenthesisequal.py
#@author  :Vikas Sharma
#***********************************************
from utility.utilMethods import is_paranthesis

paranthesis = str(input("enter the equation of the evaluate the paraenthesis"))
print(paranthesis)
lst=[]
for i in paranthesis:
    lst.append(i)
is_paranthesis(lst)
