# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        prev = dummy
        curr = head
        
        length = 0
        while curr:
            curr = curr.next
            length += 1

        remove_from_start = length - n

        curr = head
        for _ in range(remove_from_start):
            prev = curr
            curr = curr.next
        
        if curr.next:
            prev.next = curr.next
        else:
            prev.next = None
        
        return dummy.next
