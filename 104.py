#104
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # recursive and DFS approach
        # time complexity O(n)
        # space comlexity O(n) for unbalanced tree
        # space complexity O(log(n)) for a completely balanced tree
        if not root:
            return 0
        else:
            left_depth  = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return 1 + max(left_depth,right_depth)
        
        # iterative approach
        # time complexity O(n)
        # space comlexity O(n) for unbalanced tree
        # space complexity O(log(n)) for a completely balanced tree
        max_depth = 0
        stack = []
        if root:
            stack.append((1,root))
        while stack:
            
            curr_depth,node = stack.pop()
            #print("*",node.val)
            if node:
                max_depth = max(curr_depth,max_depth)
                if node.left:
                    stack.append((curr_depth+1,node.left))
                if node.right:
                    stack.append((curr_depth+1,node.right))
        return max_depth
