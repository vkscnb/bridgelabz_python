from utility.utilMethods import is_temperature

num = int(input("enter the choice  1 for celsius temperature or 0 for ferenhiet temrerature "))
if num==1:
    fer = eval(input("enter the temperature in ferhenhiet"))
    is_temperature(fer,num)

else:
    cel = eval(input("enter the temperature in celsius"))
    is_temperature(cel, num)