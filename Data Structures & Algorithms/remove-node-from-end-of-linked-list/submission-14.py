# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start_pointer = head
        end_pointer = head
        prev = None
        for i in range(n-1):
            end_pointer = end_pointer.next
        print(start_pointer.val, end_pointer.val)
       
        while(end_pointer.next is not None):
            prev = start_pointer
            end_pointer = end_pointer.next
            start_pointer = start_pointer.next
        try:
            print(start_pointer.val, prev.val, end_pointer.val)
        except:
            pass
        #end_pointer tracks the last item of the list
        #start_pointer tracks the start of it

        if prev == None:
            return head.next
        elif start_pointer == end_pointer:
            prev.next = None
        else:
            prev.next = start_pointer.next


        
        
        return head