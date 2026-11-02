# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        prev = dummy
        pointer_1 = head
        if pointer_1:
            if pointer_1.next:
                pointer_2 = head.next
            else:
                pointer_2 = None

        while pointer_1 and pointer_2:
            next_ = pointer_2.next
            pointer_2.next = pointer_1
            pointer_1.next = next_
            prev.next = pointer_2

            prev = pointer_1
            if pointer_1.next:
                pointer_2 = pointer_1.next.next
            else:
                pointer_2 = None

            pointer_1 = pointer_1.next
            

        return dummy.next
