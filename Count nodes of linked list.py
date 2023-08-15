class Node:
    def __init__(self):
        self.head=None
        self.next=None

class Solution:
    
    #Function to count nodes of a linked list.
    def getCount(self, head_node):
        count = 1
        while(head_node.next!=None):
            count += 1
            head_node = head_node.next
        return count