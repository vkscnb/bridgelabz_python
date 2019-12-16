from utility.utilMethods import is_paranthesis

paranthesis = str(input("enter the equation of the evaluate the paraenthesis"))
print(paranthesis)
lst=[]
for i in paranthesis:
    lst.append(i)
is_paranthesis(lst)
