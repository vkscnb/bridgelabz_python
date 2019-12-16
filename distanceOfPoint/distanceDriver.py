#***********************************************
#@purpose :find the distance of two points
#@file    :distanceDriver.py
#@author  :Vikas Sharma
#***********************************************
from utility.utilMethods import is_distance

print("enter the first points cordinates X1 and X2")
x1 = int(input())
x2 = int(input())
print("enter the second points cordinates Y1 and Y2")
y1 = int(input())
y2 = int(input())
is_distance(x1, x2, y1, y2)
