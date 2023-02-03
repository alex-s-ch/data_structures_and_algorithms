from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self, root):
        self.root = self.invertTree(root=root)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    def print_tree(self, root):
        if root:
            print(root.val)
            self.print_tree(root.left)
            self.print_tree(root.right)

root = TreeNode(4,
                TreeNode(2, TreeNode(1), TreeNode(3)),
                TreeNode(7, TreeNode(6), TreeNode(9)))

# input = [4, 2, 1, 3, 7, 6, 9]
# output = [4, 7, 9, 6, 2, 3, 1]
#      4                4
#   2     7          7     2
# 1  3  6   9      9  6   3  1

solution = Solution(root)
solution.print_tree(root)