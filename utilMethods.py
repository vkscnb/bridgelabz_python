import math
import random


def is_distance(x1, x2, y1, y2):
    X = (x2 - x1) ** 2
    Y = (y2 - y1) ** 2
    dis = math.sqrt((X + Y))
    print(dis)


def is_Prime(num):
    count = 1
    for i in range(2, num + 1):
        if (num % i == 0):
            count += 1

    if (count == 2):
        return True

    return False


def is_primeFactors(n):
    # Print the number of two's that divide n
    while n % 2 == 0:
        print(2)
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            print(i)
            n = n / i

            # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


def is_harmonic(num):
    hr = 1
    for i in range(1, num + 1):
        print(hr / i, end=" ")
        if (i < num):
            print("+", end=" ")


def is_leapyear(year):
    if (year >= 1582):
        if (year % 400 == 0):
            return True
        elif (year % 100 == 0):
            return False
        elif (year % 4 == 0):
            return True

    else:
        return False


def is_flipcoin(num):
    heads = 0
    tails = 0
    for i in range(1, num + 1):
        flip = random.randint(0, 1)
        if (flip == 0):
            heads += 1
        else:
            tails += 1
    print("percentage of heads= ", (heads / num) * 100)
    print("percentage of tails= ", (tails / num) * 100)


def is_quadratic(a, b, c):
    delta = b ** 2 - (4 * a * c)
    if (delta > 0):
        root1 = (-b + math.sqrt(delta)) / (2 * a)
        root2 = (-b - math.sqrt(delta)) / (2 * a)
        print("root1 is =", root1, " root2 is = ", root2)
    elif (delta == 0):
        root1 = root2 = -b / (2 * a)
        print("root1 and root2 are same= ", root1)
    else:
        real = -b / (2 * a)
        imaginary = math.sqrt(-delta) / (2 * a)
        print("Real part is =", real, "\nImaginary part is =", imaginary)


def is_gambler(stake, goal, trials):
    wins = 0
    bets = 0
    for i in range(trials):
        cash = stake
        while (cash > 0 and cash < goal):
            bets += 1
            x = random.randint(0, 1)
            if (x == 1):
                cash += 1
            else:
                cash -= 1
        if (cash == goal):
            wins += 1


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


def is_windchill(t, v):
    if (t <= 50) and (v >= 3 and v <= 120):
        wind = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16


def is_add(lst, size):
    found = True
    for i in range(0, size - 2):
        for j in range(i + 1, size - 1):
            for k in range(j + 1, size):
                if (lst[i] + lst[j] + lst[k] == 0):
                    print(lst[i], lst[j], lst[k])
                    found = True
    if (found == False):
        print("not exist")


def is_binarynum(binnum):
    binlst = []
    num = binnum
    while (binnum != 0):
        rem = binnum % 2
        binlst.append(rem)
        binnum = binnum // 2
    x = len(binlst)
    binlst2 = []
    print("Binary of a ", num, "is =", end="")
    for i in range(x - 1, -1, -1):
        print(binlst[i], end=" ")


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


def is_insertion(name):
    for i in range(1, len(name)):
        tmp = name[i]
        j = i - 1
        while (j >= 0 and name[j] > tmp):
            name[j + 1] = name[j]
            j = j - 1
        name[j + 1] = tmp
        print(name)
        print()
    return name


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


def is_temperature(degree, num):
    if num == 1:
        cels = (degree - 32) * (5 // 9)
        print("Temperature in celcius = ", cels)
    else:
        fers = degree * (9 // 5) + 32
        print("Temperature in fernhiet = ", fers)


def is_bintodec(binv):
    num = len(binv)
    sum = 0
    for i in range(num-1):
        sum += (2 * int(binv[i])) ** (num-i-1)
    i+=1
    if i ==num-1:
        if binv[i]=='0':
            sum+=0
        else:
            sum+=1
    print(sum)

def is_payment(payment,n,r):
    monthlyPayment = (payment*r)/1-(1+r)**(-n)
    return monthlyPayment

def is_anagram(str1,str2):
    str1len = len(str1)
    str2len = len(str2)
    x = sorted(str1)
    y = sorted(str2)
    count=0
    if(str1len == str2len):
        for i in range(0,str1len):
            if x[i]==y[i]:
                count+=1
        if count == str1len:
            print("String is Anagram")
        else:
            print("String is not Anagram")
    else:
        print("string not Anagram******")



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
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.start=None


    def insertlast(self,value):
        newnode =Node(value)
        if(self.start==None):
            self.start=newnode
        else:
            temp=self.start
            while temp.next !=None:
                temp=temp.next
            temp.next=newnode

    def printList(self):
        if self.start== None:
            print("list is empty")
        else:
            temp=self.start
            while temp != None:
                print(temp.data, end=" ")
                temp=temp.next

    def deleteFirst(self):
        if self.start==None:
            print("list is empty")
        else:
            self.start=self.start.next

    #delete from position

    def deleteposition(self,key):
        temp = self.start
        if temp is not None:
            if temp.data==key:
                self.start=temp.next
                temp=None
                return
        while(temp is not None):
            if temp.data == key:
                break
            prev=temp
            temp=temp.next

        if temp==None:
            return

        prev.next = temp.next

        temp=None

# stackprogram


def is_paranthesis(lst):
    stack=[]
    stackobj =Stack()
    for i in lst:
        if i=='(' or i=='{' or i== '[':
            stackobj.push(i)
            stackobj.printstack()
        elif i==')' or i=='}' or i== ']':
            stackobj.pop()
            #stackobj.printstack()

    cunt=stackobj.size()
    if cunt == 0:
        print("Paranthesis are equal")
    else:
        print("Paranthesis are not equal")
    #
    # topelement=stackobj.top()
    # print("top element= ",topelement)
    result= stackobj.isEmpty()
    print("stack is empty = ",result)

class Node1:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head = None

    # insert at first
    def push(self,data):
        if self.head is None:
            self.head = Node1(data)
        else:
            newnode = Node1(data)
            newnode.next=self.head
            self.head=newnode
    # delete  at first
    def pop(self):
        if self.head is None:
            return None
        else:
            temp=self.head
            self.head=self.head.next
            return temp

    # def top(self):
    #     return self.head.data

    def size(self):
        temp = self.head
        count=0
        while temp is not None:
            count+=1
            temp =temp.next
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
            temp=temp.next


#QUEUE Banking


def is_queue(people):
    queue = Queue()
    for i in range(0, people):
        deposit = int(input("Enter 1 for deposite or 0 for withdraw"))

        if deposit==1:
            depositemoney= eval(input("enter the amount to deposite in bank"))
            queue.enqueue(depositemoney)

        elif deposit==0:
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
        if (self.first == None):
            self.first = newnode
        else:
            temp = self.first
            while temp.next != None:
                temp = temp.next
            temp.next = newnode

    #delete at first
    def dequeue(self):
        if self.first==None:
            print("queue is empty")
        else:
            #temp = self.head
            self.first=self.first.next
            #temp=None

    def printqueue(self):
        if self.first==None:
            print("queue is Empty")
        temp = self.first
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next

###########################################################################################################
# ordered list Assending order

def is_orderList(number):
    orderlist =OrderList()
    for i in range(number):
        value = eval(input("enter the value to store in the linked list"))
        orderlist.Queue(value)
    orderlist.printQueue()



class Node3:
    def __init__(self,data):
        self.data=data
        self.next=None

class OrderList:
    def __init__(self):
        self.head=None

    def Queue(self,value):
        newnode=Node3(value)
        if self.head == None:
            self.head=newnode
        else:
            temp=self.head
            while temp.data <newnode.data:
                temp=self.head
                self.head=temp.next
            temp1=newnode
            temp1.next=temp.next
            temp.next=temp1

    def printQueue(self):
        if self.head==None:
            print("queue is Empty")
        temp = self.head
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next


#################################################################################


#palindrome linked list

def is_palindrome(str):
    palindrome=Palindrome()
    for i in str:
        palindrome.insertfirst(i)
    result=palindrome.printpalindrome()
    count=0
    for i in range(len(str)):
        if result[i]==  str[i]:
            count+=1
    if count==len(str):
        print()
        print("String is palindrome")
    else:
        print()
        print("String is not palindrome")

class Node4:
    def __init__(self,data):
        self.data=data
        self.next=None

class Palindrome:
    def __init__(self):
        self.head=None

    def insertfirst(self,val):
        if self.head==None:
            self.head=Node4(val)
        else:
            newnode=Node4(val)
            newnode.next=self.head
            self.head=newnode

    def printpalindrome(self):
        if self.head==None:
            print("list is empty")
        else:
            temp = self.head
            y=[]
            while temp != None:
                print(temp.data, end="->")
                x=temp.data
                y.append(x)
                temp = temp.next
        return y


#***************************************************************************8

# primeanagram

def is_primeQueue(Range):
    lst=[]
    for i in range(2,Range+1):
        count=0
        for j in range(1,i+1):
            if (i%j)==0:
                count+=1
        if count==2:
            lst.append(i)
    print(lst)
    is_anagramQueue(lst)


def is_anagramQueue(lst):
    lst1=[]
    lst2=[]
    for i in lst:
        lst1.append(str(i))
    print("lst1 string=",lst1)
    for i in lst1:
        if i=='2' or i=='3' or i=='5' or i=='7':
            lst2.append(int(i))
            print("lst2=",lst2)
        else:
            for j in lst1:
                #print(type(i),"->",type(j),end=" ")
                if len(i)==len(j):
                    #print(i)
                    x=sorted(i)
                    y=sorted(j)
                    count=0
                    for k in range(0,len(i)):
                        if x[k]==y[k]:
                            count+=1
                    if count==len(i):
                        lst2.append(int(i))

    print(lst2)
    primequeue=PrimeQueue()
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
        if (self.first == None):
            self.first = newnode
        else:
            temp = self.first
            while temp.next != None:
                temp = temp.next
            temp.next = newnode


    def Printqueue(self):
        if self.first==None:
            print("queue is Empty")
        temp = self.first
        while temp != None:
            print(temp.data, end="->")
            temp = temp.next

