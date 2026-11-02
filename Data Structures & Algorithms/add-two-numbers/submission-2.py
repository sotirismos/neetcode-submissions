# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_num = ""
        while l1:
            l1_num += str(l1.val)
            l1 = l1.next
        
        l1_num = int(l1_num[::-1])

        l2_num = ""
        while l2:
            l2_num += str(l2.val)
            l2 = l2.next
        
        l2_num = int(l2_num[::-1])

        total_sum = l1_num + l2_num
        total_sum = str(total_sum)[::-1]

        if len(total_sum) > 0:
            head = ListNode(val=total_sum[0])

        curr = head
        for digit in total_sum[1::]:
            curr.next = ListNode(val=digit)
            curr = curr.next
        
        return head


