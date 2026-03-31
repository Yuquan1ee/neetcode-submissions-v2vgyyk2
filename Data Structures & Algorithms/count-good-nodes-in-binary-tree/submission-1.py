# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        no_good_nodes = 0
        holding = deque()
        if not root:
            return no_good_nodes
        holding.append((root,root.val))
        no_good_nodes = 1
        while(holding):
            
            cur_node, highest_val = holding.popleft()
            if cur_node.left:
                if cur_node.left.val >= highest_val:
                    no_good_nodes +=1
                    holding.append((cur_node.left, cur_node.left.val))
                else:
                    holding.append((cur_node.left,highest_val))
            if cur_node.right:
                if cur_node.right.val >=highest_val:
                    no_good_nodes += 1
                    holding.append((cur_node.right, cur_node.right.val))
                else:
                    holding.append((cur_node.right, highest_val))
                
        return no_good_nodes

