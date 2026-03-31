# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # creating a dummy head node
        dummy = ListNode()
        cur = dummy
        cur1 = list1
        cur2 = list2
        while(cur1 != None or cur2 != None):
            if cur1 != None and cur2 != None:
                if cur1.val < cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                    cur = cur.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                    cur = cur.next
            elif  cur1 != None:
                cur.next = cur1
                cur1 = None
            else:
                cur.next = cur2
                cur2 = None
        return dummy.next
                    

        

#### MUST RETRY THIS
    
        

        
        