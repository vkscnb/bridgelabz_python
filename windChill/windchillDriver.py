#***********************************************
#@purpose :find wind is chill or not
#@file    :windchillDriver.py
#@author  :Vikas Sharma
#***********************************************
from sys import argv

from utility.utilMethods import is_windchill

t= argv[1]
v= argv[2]
is_windchill(t,v)