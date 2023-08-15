class Node:
    def __init__(self,k):
        self.data = k
        self.next = None

class Solution:
    def Sum(head):
        ans = head
        while(head.next!=None):
            head = head.next
            ans += head.data
        return ans