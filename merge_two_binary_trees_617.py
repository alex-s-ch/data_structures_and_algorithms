from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node1 and not node2:
            return None

        val1 = node1.val if node1 else 0
        val2 = node2.val if node2 else 0
        root = TreeNode(val = val1 + val2) # new node

        root.left = self.mergeTrees(node1.left if node1 else None, node2.left if node2 else None) # condition: can't take left attribute of None object
        root.right = self.mergeTrees(node1.right if node1 else None, node2.right if node2 else None)

        return root
