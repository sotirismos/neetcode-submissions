# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = 1
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            nodes += 1
        
        if fast:
            num_of_nodes = (2 * nodes) - 1
        else:
            num_of_nodes = (2 * nodes) - 2
        
        if num_of_nodes < 2:
            head = None
            return head

        steps_needed = (num_of_nodes - n)
        previous_node = None
        curr = head
        if steps_needed == 0:
            return head.next
        for counter in range(steps_needed):
            previous_node = curr
            curr = curr.next
        
        if curr.next:
            previous_node.next = curr.next
        else:
            previous_node.next = None

        return head
