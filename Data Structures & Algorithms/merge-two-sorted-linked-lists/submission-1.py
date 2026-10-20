# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr1, curr2 = list1, list2
        res = head = ListNode()

        while curr1 and curr2:

            if curr1.val < curr2.val:

                head.next = ListNode(curr1.val)
                curr1 = curr1.next
            
            else:

                head.next = ListNode(curr2.val)
                curr2 = curr2.next
        
            head = head.next
        
        if not curr1:

            head.next = curr2
        
        else:

            head.next = curr1
        
        return res.next

        