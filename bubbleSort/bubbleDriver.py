from utility.utilMethods import is_bubble

size = int(input("enter the size of the list"))
bubble=[]
for i in range(size):
    bubble.append(int(input()))
print(bubble)
is_bubble(bubble,size)