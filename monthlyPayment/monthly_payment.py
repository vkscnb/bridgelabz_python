#***********************************************
#@purpose :Calculate the monthly payment  
#@file    :monthly_payment.py
#@author  :Vikas Sharma
#***********************************************

from sys import argv

from utility.utilMethods import is_payment

payment = argv[1]
year = argv[2]
rate = argv[3]
n = 12*year
r = rate/(12*100)
monthlyPayment = is_payment(payment, n, r)
print("monthly payment of the year is = ", monthlyPayment)