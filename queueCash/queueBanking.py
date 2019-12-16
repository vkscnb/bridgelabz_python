#***********************************************
#@purpose :store bank record in a queue
#@file    :queueBanking.py
#@author  :Vikas Sharma
#***********************************************
from utility.utilMethods import is_queue

people = int(input("enter how many people in a queue"))
is_queue(people)