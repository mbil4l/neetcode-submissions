class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        
        # slow = mid
        prev, curr = None, slow.next
        slow.next = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev, curr = curr, tmp
        
        dummy = head

        while prev:
            
            left = dummy.next
            right = prev.next

            dummy.next = prev
            prev.next = left

            dummy, prev = left, right

        # return head 



        