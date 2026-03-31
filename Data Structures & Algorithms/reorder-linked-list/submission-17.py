# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return
        slow = head
        fast = head
        while(slow != None and fast != None):
            fast = fast.next
            if fast != None:
                fast = fast.next
                slow = slow.next
        
        next_node = slow.next
        slow.next = None
        slow = next_node

        #reverse link list

        prev = None
        while(slow != None):
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        print(prev.val)

        cur = head

        while (prev != None):
            next_prev = prev.next
            next_cur = cur.next
            cur.next = prev
            prev.next = next_cur
            cur = next_cur
            prev = next_prev
        
       
       


### MUST RELOOK INTO THIS NONSENSE


        
