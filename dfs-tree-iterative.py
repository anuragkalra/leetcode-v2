class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return res


def inorder(root):
	res, stack = [], []
	while stack or root:
		while root:
			stack.append(root)
			root = root.left
		root = stack.pop()
		res.append(root.val)
		root = root.right
	return res

# In post order, the root is always the final node
# Time O(n) need to visit every single node
# Space O(log n) Average case. log n = height of tree
# Space O(n) Worst case
def postorder(root):
	if not root:
            return None
	res, stack = [], [root]
	while stack:
		node = stack.pop()
		res.insert(0, node.val)
		if node.left:
			stack.append(node.left)
		if node.right:
			stack.append(node.right)
	return res


T = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
print(preorder(T))
print(inorder(T))
print(postorder(T))











