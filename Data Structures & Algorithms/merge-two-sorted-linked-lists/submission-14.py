# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # creating a dummy head node
        if list1 is None and list2 is None:
            return None
        dummy = ListNode(0)
        cur = dummy
        cur1 = list1
        cur2 = list2
        while(cur2 is not None and cur1 is not None):
            print(cur1.val,cur2.val)
            if cur1.val<cur2.val:
                cur.next = cur1
                cur1 = cur1.next
                cur = cur.next
            else:
                cur.next = cur2
                cur2 = cur2.next
                cur = cur.next
        
        if cur2 is not None:
            cur.next = cur2
        else:
            cur.next = cur1
        
        return dummy.next
        

        

        
    
        

        
        