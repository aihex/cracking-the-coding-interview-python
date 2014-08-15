import random
from BSTreeNode import BSTreeNode


def common_ancestor_1(root, n1, n2, res):
    ''' start from root and all the way down to leaf
        check if a node is a common ancestor of n1 and n2'''
    if not (root and n1 and n2):
        return None
    if is_offspring(root, n1) and is_offspring(root, n2):
        res[0] = root
        common_ancestor_1(root.left, n1, n2, res)
        common_ancestor_1(root.right, n1, n2, res)


def is_offspring(root, n1):
    if not root:
        return False
    if root == n1 or is_offspring(root.left, n1) or is_offspring(root.right, n1):
        return True


def common_ancestor_2(root, n1, n2):
    path1 = []
    path2 = []
    find_path(root, n1, path1)
    find_path(root, n2, path2)
    # print path1
    # print path2
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        else:
            i += 1
    return path1[i-1]


def find_path(root, n1, res):
    if not root:
        return False
    if root == n1:
        res.append(root)
        return True
    res.append(root)
    found = find_path(root.left, n1, res)
    if not found:
        found = find_path(root.right, n1, res)
    if not found:
        res.pop()
        return False
    return True


if __name__ == '__main__':
    array = [random.randint(0, 10) for i in xrange(20)]
    # array = [10, 9, 8, 5, 8, 5, 10, 10, 10, 6, 3, 2, 5, 2, 3, 0, 1, 0, 10, 2]
    print array
    root = BSTreeNode.create_from_array(array)
    print root.preorder_print()
    n1 = root.find(8)
    n2 = root.find(5)
    res = [0]
    if n1 and n2:
        common_ancestor_1(root, n1, n2, res)
        print res[0]
        print common_ancestor_2(root, n1, n2)
