class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal(root):
    result = []
    def helper(root, result):
        if root:
            result.append(root.val)
            helper(root.left, result)
            helper(root.right, result)
    helper(root, result)
    return result

'''
Time O(n) we need to visit every single node
Space O(n) we need to add a function to the call stack for every node
'''
def inorderTraversal(root):
    result = []
    def helper(root, result):
        if root:
            helper(root.left, result)
            result.append(root.val)
            helper(root.right, result)
    helper(root, result)
    return result

def postorderTraversal(root):
    def helper(root, result):
        if root:
            helper(root.left, result)
            helper(root.right, result)
            result.append(root.val)
    result = []
    helper(root, result)
    return result

T = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
print(preorderTraversal(T))
print(inorderTraversal(T))
print(postorderTraversal(T))