#***********************************************
#@purpose :All funtion initialize in util method
#@file    :utilMethods.py
#@author  :Vikas Sharma
#***********************************************

import math
import random

# distance between two points

def is_distance(x1, x2, y1, y2):
    X = (x2 - x1) ** 2
    Y = (y2 - y1) ** 2
    dis = math.sqrt((X + Y))
    print(dis)

#***********************************************

# find prime number 

def is_Prime(num):
    count = 1
    for i in range(2, num + 1):
        if (num % i == 0):
            count += 1

    if count is 2:
        return True

    return False

#*************************************************

# find prime factor

def is_primeFactors(number):
    # Print the number of two's that divide n
    
    while number % 2 == 0:
        print(2)
        number = number / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    
    for divisor in range(3, int(math.sqrt(number)) + 1, 2):
        divisor_other(number,divisor)
        # while i divides n , print i ad divide n

    def divisor_other(number,divisor):    
        while number % divisor == 0:
            print(divisor)
            number = number / divisor

            # Condition if n is a prime
    # number greater than 2
    
    if number > 2:
        print(number)

#********************************************************

# create harmonic series

def is_harmonic(num):
    hr = 1
    for i in range(1, num + 1):
        print(hr / i, end=" ")
        if i < num:
            print("+", end=" ")

#**********************************************************

# find the leapYeap

def is_leapyear(year):
    if year >= 1582 :
        if (year % 400) is 0:
            return True
        elif (year % 100) is 0:
            return False
        elif (year % 4) is 0:
            return True

    else:
        return False

#***********************************************************

# find the percentage of flip coin(head and tails)

def is_flipcoin(number):
    heads = 0
    tails = 0
    for num in range(1, number + 1):
        flip = random.randint(0, 1)
        if flip is 0:
            heads = heads + 1
        else:
            tails = tails + 1
    print("percentage of heads= ", (heads / number) * 100)
    print("percentage of tails= ", (tails / number) * 100)

#*************************************************************

# find the quadratic equation
 
def is_quadratic(a, b, c):
    delta = b ** 2 - (4 * a * c)
    if delta > 0 :
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("root1 is =", root1, " root2 is = ", root2)
    elif delta is 0:
        root1 = root2 = -b / (2 * a)
        print("root1 and root2 are same= ", root1)
    else:
        real = -b / (2 * a)
        imaginary = math.sqrt(-delta) / (2 * a)
        print("Real part is = ", real, "\nImaginary part is =", imaginary)

#**************************************************************

# calculate the gabler win or loose

def is_gambler(stake, goal, trials):
    global wins, bets
    wins = 0
    bets = 0
    for _ in range(trials):
        cash = stake
        check_cash(cash)
    
    def check_cash(cash):
        if (cash > 0) and (cash < goal):
            bets = bets + 1
            x = random.randint(0, 1)
            if x is 1:
                cash = cash + 1
            else:
                cash = cash - 1
        if cash is goal:
            wins = wins + 1

#****************************************************

# find the random coupon number

def is_coupon(num):
    arr = []
    arr1 = []
    for i in range(0, num):
        ran = random.randint(0, 9)
        arr.append(ran)
    print(arr)
    for i in arr:
        if (i not in arr1):
            arr1.append(i)
    print(arr1)
    print("Distinct coupon in a coupon", len(arr1))

#****************************************************

# find the wind temperature

def is_windchill(temperature, velocity):
    if (temperature <= 50) and (velocity >= 3) and (velocity <= 120):
        wind = 35.74 + 0.6215 * temperature + (0.4275 * temperature - 35.75) * velocity ** 0.16
        print(wind)
#*****************************************************

# calculate the sum of three pairs in a list is zero

def is_add(lst, size):
    found = True
    for i in range(0, size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j + 1, size):
                if (lst[i] + lst[j] + lst[k]) is 0:
                    print(lst[i], lst[j], lst[k])
                    found = True
    if found is False:
        print("not exist")

#******************************************************

# convert binary to decimal

def is_binarynum(binary_number):
    binary_list = []
    num = binary_number
    while (binary_number != 0):
        rem = binary_number % 2
        binary_list.append(rem)
        binary_number = binary_number // 2
    x = len(binary_list)
    
    print("Binary of a ", num, "is =", end="")
    for i in range(x - 1, -1, -1):
        print(binary_list[i], end=" ")

#******************************************************

# program for bubble sort

def is_bubble(bubble, size):
    for i in range(size):
        flag = 0
        for j in (0, size - i - 1):
            if (bubble[j] > bubble[j + 1]):
                bubble[j], bubble[j + 1] = bubble[j + 1], bubble[j]
                flag = 1
        if (flag == 0):
            break
    print(bubble)

#******************************************************

# program for insertion sort

def is_insertion(name_lst):
    for i in range(1, len(name_lst)):
        tmp = name_lst[i]
        j = i - 1
        check_string(tmp,j)
    def check_string(tmp,j):
        if (j >= 0 and name_lst[j] > tmp):
            name_lst[j + 1] = name_lst[j]
            j = j - 1
        name_lst[j + 1] = tmp
        print(name_lst)
        print()
    return name_lst

#********************************************************

# program for binary search 

def is_binarySearch(arr, search, intsearch):
    low = 0
    high = len(arr)
    arr1 = is_insertion(arr)
    print(arr1)
    srch = int(input("press 1 for string binary search or other for number binary search"))
    if srch == 1:
        while (low <= high):
            m = (low + high) // 2

            res = (search == arr1[m])

            # Check if x is present at mid
            if (res == 0):
                return m - 1

            # If x greater, ignore left half
            if (res > 0):
                low = m + 1

            # If x is smaller, ignore right half
            else:
                high = m - 1
    else:
        while (low <= high):
            m = (low + high) // 2

            res = (intsearch == arr1[m])

            # Check if x is present at mid
            if (res == 0):
                return m - 1

            # If x greater, ignore left half
            if (res > 0):
                low = m + 1

            # If x is smaller, ignore right half
            else:
                high = m - 1

    return -1

#**********************************************************

# program for merge sort

def is_mergesort(arr, num):
    low = 0
    high = num
    mid = (low + high) // 2
    arr1 = []
    i = 0
    j = mid + 1
    k = low
    while i <= mid and j <= high:
        if (arr[i] < arr[j]):
            arr1[k].append(arr[i])
            k += 1
            i += 1
        else:
            arr1[k].append(arr[j])
            k += 1
            j += 1
    for i in range(i, mid + 1):
        arr1[k].append(arr[i])
        k += 1
    for j in range(j, high):
        arr1[k].append(arr[j])
        k += 1
    # for i in range(0,high):
    #     arr[i].append(arr1[i])
    print("merge array is ", arr1)

#*********************************************************

# calculate the  temperature

def is_temperature(degree, num):
    if num == 1:
        cels = (degree - 32) * (5 // 9)
        print("Temperature in celcius = ", cels)
    else:
        fers = degree * (9 // 5) + 32
        print("Temperature in fernhiet = ", fers)

#**********************************************************

# program for binary to decimal

def is_bintodec(binv):
    num = len(binv)
    sum = 0
    for i in range(num-1):
        sum = sum + (2 * int(binv[i])) ** (num-i-1)
    i = i+1
    if i is num-1:
        if binv[i] is '0':
            sum = sum + 0
        else:
            sum = sum + 1
    print(sum)

#***********************************************************

# calculate the payment

def is_payment(payment,n,r):
    monthlyPayment = (payment*r)/1-(1+r)**(-n)
    return monthlyPayment

#***********************************************************

# program for string anagram

def is_anagram(str1,str2):
    str1len = len(str1)
    str2len = len(str2)
    x = sorted(str1)
    y = sorted(str2)
    count=0
    if(str1len is str2len):
        for i in range(0,str1len):
            if x[i] is y[i]:
                count = count + 1
        if count is str1len:
            print("String is Anagram")
        else:
            print("String is not Anagram")
    else:
        print("string not Anagram******")

#************************************************************

# Read the file and store in the linked list 

def is_readText(path):
    data = open(path,"r")
    lst=[]
    lst2 = []
    for line in data.readlines():
        lst.append([line])
        for i in line.split():
            lst2.append(i)
    print(lst)

    # insert in to linked list
    linkedList = LinkedList()
    for i in lst2:
        linkedList.insertlast(i)

    print("List after spliting", lst2)
    word = input("enter the word to search in file")
    if word in lst2:
        lst2.remove(word)
        linkedList.deleteposition(word)
    else:
        lst2.append(word)
        linkedList.insert(word)

      # print the linked list
    linkedList.printList()


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.start = None


    def insertlast(self,value):
        newnode = Node(value)
        if(self.start is None):
            self.start = newnode
        else:
            temp = self.start
            while temp.next is None:
                temp = temp.next
            temp.next = newnode

    def printList(self):
        if self.start is None:
            print("list is empty")
        else:
            temp = self.start
            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

    def deleteFirst(self):
        if self.start == None:
            print("list is empty")
        else:
            self.start = self.start.next

    #delete from position

    def deleteposition(self,key):
        temp = self.start
        if temp is not None:
            if temp.data == key:
                self.start = temp.next
                temp = None
                return
        while(temp is not None):
            if temp.data is key:
                break
            prev = temp
            temp = temp.next

        if temp==None:
            return

        prev.next = temp.next

        temp=None

#***************************************************

# calculate the parenthesis are equal or not in stack

def is_paranthesis(lst):
    stack = []
    stackobj = Stack()
    for i in lst:
        if i is '(' or i is '{' or i is '[':
            stackobj.push(i)
            stackobj.printstack()
        elif i is ')' or i is '}' or i is ']':
            stackobj.pop()
            #stackobj.printstack()

    cunt = stackobj.size()
    if cunt is 0:
        print("Paranthesis are equal")
    else:
        print("Paranthesis are not equal")
    #
    # topelement=stackobj.top()
    # print("top element= ",topelement)
    result = stackobj.isEmpty()
    print("stack is empty = ", result)

class Node1:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    # insert at first
    def push(self,data):
        if self.head is None:
            self.head = Node1(data)
        else:
            newnode = Node1(data)
            newnode.next = self.head
            self.head = newnode
    # delete  at first
    def pop(self):
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            return temp

    # def top(self):
    #     return self.head.data

    def size(self):
        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False

    def printstack(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

#**************************************************************

# program for bank diposite and withdraw program using QUEUE


def is_queue(people):
    queue = Queue()
    for i in range(0, people):
        deposit = int(input("Enter 1 for deposite or 0 for withdraw"))

        if deposit is 1:
            depositemoney = eval(input("enter the amount to deposite in bank"))
            queue.enqueue(depositemoney)

        elif deposit is 0:
            queue.dequeue()

        queue.printqueue()


class Node2:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first =  None


    #insert at last
    def enqueue(self,value):
        newnode = Node2(value)
        if (self.first is None):
            self.first = newnode
        else:
            temp = self.first
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode

    #delete at first
    def dequeue(self):
        if self.first is None:
            print("queue is empty")
        else:
            #temp = self.head
            self.first = self.first.next
            #temp=None

    def printqueue(self):
        if self.first==None:
            print("queue is Empty")
        temp = self.first
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next

###########################################################################################################

# program for ordered list Assending order using linked list

def is_orderList(number):
    orderlist = OrderList()
    for i in range(number):
        value = eval(input("enter the value to store in the linked list"))
        orderlist.Queue(value)
    orderlist.printQueue()



class Node3:
    def __init__(self,data):
        self.data = data
        self.next = None

class OrderList:
    def __init__(self):
        self.head = None

    def Queue(self,value):
        newnode = Node3(value)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.data < newnode.data:
                temp = self.head
                self.head = temp.next
            temp1 = newnode
            temp1.next = temp.next
            temp.next = temp1

    def printQueue(self):
        if self.head==None:
            print("queue is Empty")
        temp = self.head
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next


#################################################################################


# program for palindrome linked list

def is_palindrome(str):
    palindrome = Palindrome()
    for i in str:
        palindrome.insertfirst(i)
    result = palindrome.printpalindrome()
    count = 0
    for i in range(len(str)):
        if result[i] is  str[i]:
            count = count + 1
    if count is len(str):
        print()
        print("String is palindrome")
    else:
        print()
        print("String is not palindrome")

class Node4:
    def __init__(self,data):
        self.data = data
        self.next = None

class Palindrome:
    def __init__(self):
        self.head = None

    def insertfirst(self,val):
        if self.head is None:
            self.head = Node4(val)
        else:
            newnode = Node4(val)
            newnode.next = self.head
            self.head = newnode

    def printpalindrome(self):
        if self.head is None:
            print("list is empty")
        else:
            temp = self.head
            y = []
            while temp is not None:
                print(temp.data, end="->")
                x = temp.data
                y.append(x)
                temp = temp.next
        return y


#*************************************************************************************

# find the prime number and find anagram to prime number and store in the linked list

def is_primeQueue(Range):
    lst = []
    for i in range(2,Range+1):
        count = 0
        for j in range(1,i+1):
            if (i%j) is 0:
                count = count + 1
        if count is 2:
            lst.append(i)
    print(lst)
    is_anagramQueue(lst)


def is_anagramQueue(lst):
    lst1 = []
    lst2 = []
    for i in lst:
        lst1.append(str(i))
    print("lst1 string = ", lst1)
    for i in lst1:
        if i is '2' or i is '3' or i is '5' or i is '7':
            lst2.append(int(i))
            print("lst2=",lst2)
        else:
            for j in lst1:
                #print(type(i),"->",type(j),end=" ")
                if len(i) is len(j):
                    #print(i)
                    x = sorted(i)
                    y = sorted(j)
                    count = 0
                    for k in range(0,len(i)):
                        if x[k] is y[k]:
                            count = count + 1
                    if count is len(i):
                        lst2.append(int(i))

    print(lst2)
    primequeue = PrimeQueue()
    for i in lst:
        primequeue.pqueue(i)
    primequeue.Printqueue()



class Node5:
    def __init__(self,data):
        self.data = data
        self.next = None

class PrimeQueue:
    def __init__(self):
        self.first =  None


    #insert at last
    def pqueue(self,value):
        newnode = Node5(value)
        if self.first is None:
            self.first = newnode
        else:
            temp = self.first
            while temp.next != None:
                temp = temp.next
            temp.next = newnode


    def Printqueue(self):
        if self.first is None:
            print("queue is Empty")
        temp = self.first
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next

