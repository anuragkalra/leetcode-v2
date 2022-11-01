class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
	res, stack = [], []
	while stack or root:
		while root:
			res.append(root.val)
			stack.append(root)
			root = root.left
		root = stack.pop()
		root = root.right
	return res


def preorder2(root):
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


def postorder(root):
    res, stack = [], [(root, False)]
    while stack:
        node, visited = stack.pop()
        if node:
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))
    return res

T = TreeNode(1, right=TreeNode(2, left=TreeNode(3)))
print(preorder(T))
# print(preorder2(T))
print(inorder(T))
print(postorder(T))











