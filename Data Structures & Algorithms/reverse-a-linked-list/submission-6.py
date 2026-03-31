# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        prev_node = None
        cur = head
       
        while(cur.next is not None):
            print(cur.val)
            next_cur = cur.next
            cur.next = prev_node
            prev_node = cur
            cur = next_cur
        cur.next = prev_node
        return cur


            