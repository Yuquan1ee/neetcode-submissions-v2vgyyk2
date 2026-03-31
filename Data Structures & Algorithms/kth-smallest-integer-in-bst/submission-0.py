# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #definitely require dfs 
        holding = []
        def dfs(root):
            nonlocal holding
            if not root or len(holding) == k:
                return None
            if dfs(root.left):
                dfs(root.left)
            holding.append(root.val)
            if dfs(root.right):
                dfs(root.right)

        dfs(root)
        return holding[k-1]