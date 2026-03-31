# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        current_val = -10000
        result = True
        def dfs(root):
            nonlocal current_val
            nonlocal result
            if not root:
                return None
            dfs(root.left)
            if root.val >current_val:
                current_val = root.val
            else:
                result = False
                return
            dfs(root.right)
        dfs(root)
        return result


# im cracked AF