# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num_1 = ""
        num_2 = ""
        while l1 or l2:
            if l1:
                num_1 += str(l1.val)
                l1 = l1.next
            if l2:
                num_2 += str(l2.val)
                l2 = l2.next
        output = int(num_1[::-1]) + int(num_2[::-1])
        output_reversed = str(output)[::-1]
        dummy = ListNode()
        head = dummy
        dummy.next = output_reversed[0]
        for val in output_reversed:
            dummy.next = ListNode(val)
            dummy = dummy.next

        return head.next