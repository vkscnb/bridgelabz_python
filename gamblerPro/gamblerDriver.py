#***********************************************
#@purpose :program for gambler wins or loss
#@file    :gamblerDriver.py
#@author  :Vikas Sharma
#***********************************************
from utility.utilMethods import is_gambler

stake=int(input("enter the value of stakes"))
goal=int(input("enter the value of goals"))
trials=int(input("enter the value of trials"))

is_gambler(stake,goal,trials)