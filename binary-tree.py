class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):
    if not root:
        return 0
    if not root.left or not root.right:
        return minDepth(root.left) + minDepth(root.right) + 1
    return min(minDepth(root.right), minDepth(root.left)) + 1

def maxDepth(root):
    if not root: 
        return 0 
    else: 
        left_height = maxDepth(root.left) 
        right_height = maxDepth(root.right) 
    return max(left_height, right_height) + 1


T = TreeNode(3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7)))
print(minDepth(T))
print(maxDepth(T))