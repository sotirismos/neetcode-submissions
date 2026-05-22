# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        counter = 0
        while first:
            first = first.next
            counter += 1
         
        target = counter - n 
        second = head

        if target == 0:
            return head.next
        
        for i in range(target):
            if i == target - 1:
                second.next = second.next.next
                break
            second = second.next
        
        return head