# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        holding_list = []
        holding_list_p = []
        holding_list_q = []
        def dfs(root):
            nonlocal holding_list 
            nonlocal holding_list_p
            nonlocal holding_list_q
            if root:
                holding_list.append(root) 
                if root.val == p.val:                    
                    holding_list_p = holding_list.copy()
                if root.val == q.val:
                    holding_list_q = holding_list.copy()
            if not root:
                holding_list.append(TreeNode(0))
                return None
            
            dfs(root.left)
            holding_list.pop()
            dfs(root.right)
            holding_list.pop()

        dfs(root)
        for i in range(min(len(holding_list_p), len(holding_list_q))-1, -1, -1):
            if holding_list_q[i].val == holding_list_p[i].val:
                return holding_list_q[i]

            
        
