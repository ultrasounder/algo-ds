def inorderTraversal(root):
    stk = []  # create a stack to push all the nodes we have seen thus far
    inorder = []  # a list to pop off items to create inorder
    node = root  # make the current node the root
    while root or stk:  # as long as there is a root node is valid
        # we add the node element and continue down the traversal
        stk.append(root)
        node = node.left  # pivot towards the left node sub-tree and continue to

        node = stk.pop()
        inorder.append(node.val)
        node = node.right
    return inorder
