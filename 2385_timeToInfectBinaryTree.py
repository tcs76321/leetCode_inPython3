# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        # class wide var for tracking final result
        self.max_distance = 0

    # main function of solution, calls traverse once, traverse sets global max dist to then return
    def amountOfTime(self, root, start):
        self.traverse(root, start)
        return self.max_distance

    def traverse(self, root, start):
        depth = 0 # start with an assumed depth of zero
        if root is None: # base case
            return depth

        # recurse to just past each leaf as above
        left_depth = self.traverse(root.left, start)
        right_depth = self.traverse(root.right, start)

        if root.val == start:
            self.max_distance = max(left_depth, right_depth)  # set our result global var to longest side
            depth = -1
        elif left_depth >= 0 and right_depth >= 0:
            depth = max(left_depth, right_depth) + 1
        else:  # 
            distance = abs(left_depth) + abs(right_depth)  # abs because couple be negative, which would be dist from start to root
            self.max_distance = max(self.max_distance, distance)
            depth = min(left_depth, right_depth) - 1

        return depth  # returning this is only used upon recursion


# This one made my brain hurt, took answer from leetcode 'editorial'.
