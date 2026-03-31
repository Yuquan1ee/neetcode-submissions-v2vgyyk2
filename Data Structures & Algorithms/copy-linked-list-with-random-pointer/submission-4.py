"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head:
            cur2 = Node(head.val)
        else:
            return None
        hash_map = {head:cur2}
        cur = head
        cur = cur.next
        
        while(cur):
            new_node = Node(cur.val)
            hash_map[cur] = new_node
            cur2.next = new_node
            cur2 = cur2.next
            cur = cur.next

        cur = head
        while(cur):
            if cur.random is None:
                hash_map[cur].random = None
            else:
                hash_map[cur].random = hash_map[cur.random]
            cur = cur.next
        return hash_map[head]