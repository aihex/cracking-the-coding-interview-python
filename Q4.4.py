from TreeNode import TreeNode


def link_level(root):
    if not root:
        return root
    q = [root, None]
    res = []
    tmp = []
    while q:
        node = q.pop(0)
        if not node:
            res.append(tmp)
            tmp = []
            if not q:
                break
            else:
                q.append(None)
            node = q.pop(0)
        tmp.append(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return res

if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3

    print link_level(n1)
