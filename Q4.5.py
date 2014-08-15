from TreeNode import TreeNode


def find_successor(node):
    if not node:
        return None
    if node.right:
        tmp = node.right
        while tmp.left:
            tmp = tmp.left
        return tmp.val
    else:
        tmp = node
        while tmp.parent and tmp == tmp.parent.right:
            tmp = tmp.parent
        if not tmp.parent:
            return None
        return tmp.parent.val


def find_predecessor(node):
    if not node:
        return None
    if node.left:
        tmp = node.left
        while tmp.right:
            tmp = tmp.right
        return tmp.val
    else:
        tmp = node
        while tmp.parent and tmp == tmp.parent.left:
            tmp = tmp.parent
        if not tmp.parent:
            return None
        return tmp.parent.val

if __name__ == '__main__':
    # print find_successor(None)
    n1 = TreeNode(8)
    n2 = TreeNode(2)
    n1.left = n2
    n2.parent = n1
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n2.right = n4
    n4.parent = n2
    n4.left = n3
    n3.parent = n4
    n6 = TreeNode(6)
    n5 = TreeNode(5)
    n4.right = n6
    n6.parent = n4
    n6.left = n5
    n5.parent = n6
    n7 = TreeNode(7)
    n6.right = n7
    n7.parent = n6

    print find_successor(n1)
    print find_successor(n2)
    print find_successor(n3)
    print find_successor(n4)
    print find_successor(n5)
    print find_successor(n6)
    print find_successor(n7)

    print

    print find_predecessor(n1)
    print find_predecessor(n2)
    print find_predecessor(n3)
    print find_predecessor(n4)
    print find_predecessor(n5)
    print find_predecessor(n6)
    print find_predecessor(n7)
