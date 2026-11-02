# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the center of the linked list
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        center = slow
        
        # Reverse the second half of the linked list
        prev = None
        curr = center
        while curr:
            next_ = curr.next
            curr.next = prev
            prev = curr
            curr = next_

        # Merge the 2 linked lists
        curr = head
        pointer_1 = head.next
        pointer_2 = prev
        counter = 0
        while pointer_1 != center and pointer_2 != center:
            if counter % 2 == 0:
                curr.next = pointer_2
                pointer_2 = pointer_2.next
            else:
                curr.next = pointer_1
                pointer_1 = pointer_1.next
            curr = curr.next
            counter += 1

        if pointer_1 == center:
            curr.next = pointer_2
        else:
            curr.next = pointer_1
        


