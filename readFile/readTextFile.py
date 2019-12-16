#**************************************************
#@purpose :read file and stored in a linked list
#@file    :readTextFile.py
#@author  :Vikas Sharma
#**************************************************
from utility.utilMethods import is_readText

openfile = open('LOOKHERE.txt', 'a+')
openfile.close()
path="/home/vkscnb/fundamentalPythonPrograms/dataStructure/readFile/LOOKHERE.txt"
is_readText(path)