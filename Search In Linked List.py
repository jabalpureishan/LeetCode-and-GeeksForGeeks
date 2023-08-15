class Node:
    def __init__(self,k):
        self.data = k
        self.next = None

class Solution:
    def search(head,x):
        if head.data==x:
            return True
        while(head.next!=None):
            head.next = next
            if head.data==x:
                return True
        return False