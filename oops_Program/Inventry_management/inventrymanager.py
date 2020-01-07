#*****************************************************
# @purpose :Read the Json File.
# @file  :inventormanager.py
# @author :Vikas Sharma
#*****************************************************

import json
import inventryfactor

class Inventory:
    def iventoryCal(self):
        #Reading JSON from a File
        with open('/home/user/Videos/test/bridgelabz_python/oops_Program/Inventry_management/inventry_json.json','r') as f:

            #read string from JSON & storing in variable
            data = json.load(f)
            print(data)

obj = Inventory()
obj.iventoryCal()