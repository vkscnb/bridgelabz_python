#*************************************************************************
#@purpose : Read the Json file and calculate the price of the items
#@file : json_inventry_calculate.py
#@author: Vikas Sharma
#*************************************************************************

import re
from datetime import datetime

read_file = open("/home/user/Videos/test/bridgelabz_python/oops_Program/regular_expresion/text_file/text.txt", "r")
write_file = open("/home/user/Videos/test/bridgelabz_python/oops_Program/regular_expresion/text_file/write.txt", "w")

first_name = input("Enter the firstname")
full_name = input("Enter the full name")

for line in read_file:
    match_first_name = re.sub('<<name>>', first_name, line)
    match_full_name = re.sub('<<full name>>', full_name, line)
    match_mobile_number = re.sub('91-[x]{10}', '91-[0-9]{10}', line)
    match_date = re.sub('[0-2][0-9]|/[0-1][0-2]/[0-9]{4}', first_name, line)


print(datetime.now())