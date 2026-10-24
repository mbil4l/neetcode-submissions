class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.head = ListNode() # dummy node

    def get(self, index: int) -> int:
        
        curr = self.head.next

        for i in range(index):
            if not curr: break 
            curr = curr.next

        return curr.val if curr else -1
        

    def addAtHead(self, val: int) -> None:

        newHead = ListNode(val, self.head.next)
        self.head.next = newHead
    def addAtTail(self, val: int) -> None:

        curr = self.head

        while curr.next:
            curr = curr.next
        
        curr.next = ListNode(val, None)

    def addAtIndex(self, index: int, val: int) -> None:

        curr = self.head

        for i in range(index):

            if not curr:
                return
            curr = curr.next
        
        curr.next = ListNode(val, curr.next)

    def deleteAtIndex(self, index: int) -> None:
        
        curr = self.head

        for i in range(index):
            if not curr.next:
                return
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)