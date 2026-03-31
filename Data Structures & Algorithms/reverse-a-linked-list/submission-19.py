# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur1 = head
        while(cur1 is not None):
            next_node = cur1.next
            cur1.next = prev
            prev = cur1
            cur1 = next_node

        return prev
#### MUST REGRIND THIS 