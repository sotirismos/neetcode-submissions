# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first_slow = head
        first_fast = head
        while first_fast and first_fast.next:
            first_slow = first_slow.next
            first_fast = first_fast.next.next

        second_curr_previous = None
        second_curr = first_slow.next
        first_slow.next = None
        while second_curr:
            second_curr_next = second_curr.next
            second_curr.next = second_curr_previous
            second_curr_previous = second_curr
            second_curr = second_curr_next

        head_first_part = head
        head_second_part = second_curr_previous
        while head_second_part:
            first_part_next = head_first_part.next
            second_part_next = head_second_part.next
            head_first_part.next = head_second_part
            head_second_part.next = first_part_next
            head_first_part = first_part_next
            head_second_part = second_part_next
