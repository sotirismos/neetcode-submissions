# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_curr = l1
        l2_curr = l2

        first_num = ""
        while l1_curr:
            first_num += str(l1_curr.val)
            l1_curr = l1_curr.next
        
        second_num = ""
        while l2_curr:
            second_num += str(l2_curr.val)
            l2_curr = l2_curr.next

        final_num = int(first_num[::-1]) + int(second_num[::-1])
        final_num = str(final_num)
        final_num = final_num[::-1]

        for index, num in enumerate(final_num):
            if index == 0:
                new_head = ListNode(val=num)
                new_curr = new_head
                
            if (index + 1) < len(final_num):
                new_curr.next = ListNode(val=final_num[index + 1])
                new_curr = new_curr.next
            else:
                new_curr.next = None
        
        return new_head