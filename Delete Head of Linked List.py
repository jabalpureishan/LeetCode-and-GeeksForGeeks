class node:
    def __init__(self,data):
        self.data = data
        self.next = None


def delete(head):
    temp = head.next
    head.next = None
    return temp
