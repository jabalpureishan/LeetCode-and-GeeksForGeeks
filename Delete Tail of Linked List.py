class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def delete(head):
    temp = head
    while(temp.next!=None):
        before = temp
        temp = temp.next
    before.next = None
    return head
