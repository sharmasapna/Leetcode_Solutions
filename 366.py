#366
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        final_res = []

            
        def dfs(node):
            if not node:
                return
            if node:
                if not node.left and not node.right:
                    res.append(node.val)
                    return None
                node.left = dfs(node.left)
                node.right = dfs(node.right)
                return node
        while (root):
            root = dfs(root)
            final_res.append(res)
            res =[]
            
        return final_res    
