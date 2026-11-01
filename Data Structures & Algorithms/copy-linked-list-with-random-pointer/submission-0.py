"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:

    def printList(self, head):

        while head:
            print(head.val, end = "->")
            head = head.next

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head
        new = dummy = Node(0)
        oldtoNew = {None: None}

        while curr:
            dummy.next = Node(curr.val)
            oldtoNew[curr] = dummy.next
            curr = curr.next
            dummy = dummy.next
        
        curr = head
        dummy = new.next
        while curr:
            dummy.random = oldtoNew[curr.random]
            curr = curr.next
            dummy = dummy.next
        
        return new.next


            
        