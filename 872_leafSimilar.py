# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leaves(self, node) -> list:
        if node is None:
            return []
        if node.left is None and node.right is None:
            return [node.val]
        return self.get_leaves(node.left) + self.get_leaves(node.right)

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves_of_1 = self.get_leaves(root1)
        leaves_of_2 = self.get_leaves(root2)
        return leaves_of_1 == leaves_of_2


# Runtime
# 41
# ms
# Beats
# 48.55%
# of users with Python3
# Memory
# 17.43
# MB
# Beats
# 7.47%
# of users with Python3
