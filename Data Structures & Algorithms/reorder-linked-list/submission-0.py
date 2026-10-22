# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head: return head

        dummy = slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow = mid, list2 = slow.next reverse(slow.next) onwards
        
        prev, curr = None, slow.next
        slow.next = None

        while curr:

            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        
        while prev:

            next = dummy.next
            prevnxt = prev.next

            dummy.next = prev
            prev.next = next
            dummy, prev = next, prevnxt
