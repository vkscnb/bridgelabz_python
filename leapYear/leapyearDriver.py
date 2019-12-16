from utility.utilMethods import is_leapyear

year=int(input("enter the year"))
result=is_leapyear(year)
if result==1:
    print("year is leap year")
else:
    print("year is not a leap year")