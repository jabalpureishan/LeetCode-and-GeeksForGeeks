class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
    
def makelist(elements):
    head = Node(elements[0])
    command = "head.next"
    for i in range(1,len(elements)):
        exec(command+"=Node("+str(elements[i])+")")
        command += ".next"
    return head

def makelist2(elements):
    head = Node(elements[0])
    curr = head
    for i in range(1,len(elements)):
        curr.next = Node(elements[i])
        curr = curr.next
    return head
        

def display(head):
    array = [head.val]
    while(head.next!=None):
        print("*")
        head = head.next
        array.append(head.val)
        
    return array

def intput():
    elements = tuple(map(int,input("").split()))
    first = makelist2(elements)
    print(first)
    return display(first)

print(intput())
    
