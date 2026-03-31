# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        holding = deque()
        holding.append(root)
        ans = []
        if not root:
            return ans
        while(holding):
            level = []
            for i in range(0, len(holding)):
                cur_node = holding.popleft()
                level.append(cur_node.val)
                if cur_node.left:
                    holding.append(cur_node.left)
                if cur_node.right:
                    holding.append(cur_node.right)
            ans.append(level[-1])
        
        return ans