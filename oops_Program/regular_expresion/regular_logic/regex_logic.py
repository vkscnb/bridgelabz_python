#*************************************************************************
#@purpose : Read the Json file and calculate the price of the items
#@file : json_inventry_calculate.py
#@author: Vikas Sharma
#*************************************************************************

import re
import datetime

class RegularExpression:

    def regular_expression(self):
            
        # read the data from file 

        read_file = open("/home/user/Videos/test/bridgelabz_python/oops_Program/regular_expresion/text_file/text.txt", "r+")
        line = read_file.read() 

        # enter the fist name, full name, and mobile number from the user

        first_name = input("Enter the firstname")
        full_name = input("Enter the full name")
        mobile_number = input("enter the mobile number with ")

        #check the regular expression and replace the user input value 
        data_update = re.sub('[<]{2}[a-zA-Z]{4}[>]{2}', first_name, line)
        data_update = re.sub('[<]{2}[a-zA-Z]{8}[>]{2}', full_name, data_update)
        data_update = re.sub('[x]{10}', mobile_number, data_update)

        date_today = str(datetime.date.today())
        data_update = re.sub('01/01/2016', date_today ,data_update)

        # open the second file for write the updated data

        output_data = open("/home/user/Videos/test/bridgelabz_python/oops_Program/regular_expresion/text_file/write.txt", "w")
        output_data.write(data_update)

        # close the all file 
        read_file.close()
        output_data.close()

regular_express = RegularExpression()
regular_express.regular_expression


