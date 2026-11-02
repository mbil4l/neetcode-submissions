# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)

        if not dummy.next:
            return None
        
        curr = dummy
        
        total = -1
        while curr:
            curr = curr.next
            total += 1

        curr = dummy
        for i in range(total - n):
            curr = curr.next
        
        curr.next = curr.next.next

        return dummy.next


