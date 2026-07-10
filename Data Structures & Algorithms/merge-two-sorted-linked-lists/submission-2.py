# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current_pointer_new = dummy

        current_pointer_1 = list1
        current_pointer_2 = list2

        while current_pointer_1 and current_pointer_2:
            if current_pointer_1.val <= current_pointer_2.val:
                current_pointer_new.next = current_pointer_1
                current_pointer_new = current_pointer_new.next 
                current_pointer_1 = current_pointer_1.next
            else:
                current_pointer_new.next = current_pointer_2
                current_pointer_new = current_pointer_new.next 
                current_pointer_2 = current_pointer_2.next
            
        if current_pointer_1:
            while current_pointer_1:
                current_pointer_new.next = current_pointer_1
                current_pointer_new = current_pointer_new.next
                current_pointer_1 = current_pointer_1.next
 
        if current_pointer_2:
            while current_pointer_2:
                current_pointer_new.next = current_pointer_2
                current_pointer_new = current_pointer_new.next
                current_pointer_2 = current_pointer_2.next

        return dummy.next 

