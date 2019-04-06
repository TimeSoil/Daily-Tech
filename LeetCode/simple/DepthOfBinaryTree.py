# IP of code : https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/solution/
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solutions:
    def maxDepth_recursive(self, root: TreeNode) -> int:


        if root == None:
            return 0
        lH = self.maxDepth(root.left)
        rH = self.maxDepth(root.right)

        return lH+1 if lH > rH else rH+1


    def maxDepth_iteration(self, root: TreeNode) -> int:
        if root == None:
            return 0

        stack = []
        stack.append((1, root))
        depth = 0

        while (stack != []):
            currentDepth, root = stack.pop()
            if root != None:
                depth = depth if depth > currentDepth else currentDepth
                stack.append((currentDepth + 1, root.left))
                stack.append((currentDepth + 1, root.right))
        return depth