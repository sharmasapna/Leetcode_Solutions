#938
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        # defining self.rsum so that it can be accessed from the function dfs
        self.rsum = 0
        
        def dfs(node,low,high):
            if node:
                # checking whether the node value is in range
                # and adding it if it is within range
                if high >= node.val >= low:
                    self.rsum += node.val
                # since it is a BST, if node value is > low,
                # there might be values greated than low which we need to add, so we traverse the left branch
                if node.val > low:
                    dfs(node.left,low,high)
                # since it is a BST, if node value is < high,
                # there might be values lesser than high which we need to add, so we traverse the right branch
                if node.val < high:
                    dfs(node.right,low,high)
            
        dfs(root,low,high)
        return self.rsum
    
# check the flow
#     at node 10 we have dfs(5,low,high) and dfs(15,low,high).
#     at node 5  we have dfs(7,low,high) as 5>7 is false and 5<15 is true
#     at node 7 we proceed no where , as it is the leaf node
#     at node 15 we do not proceed forward as 15>7 directs to left node(null) and 15<15 is false
            
            
