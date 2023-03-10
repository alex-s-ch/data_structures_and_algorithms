"""
Given a binary tree, determine if it is height-balanced. The left and right subtrees of every node differ in height by no more than 1.
"""
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1) # check if the entire tree is balanced
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0] # return only boolean

root = TreeNode(1,
                TreeNode(2,
                         TreeNode(3, None, None),
                         TreeNode(3, TreeNode(4), TreeNode(4))),
                TreeNode(2)
                )

solution = Solution()
result = solution.isBalanced(root)
print(result)
