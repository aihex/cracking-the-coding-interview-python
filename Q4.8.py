from TreeNode import TreeNode


def sum_path(root, leftover, res, arr):
    if root.val == leftover:
        res.append(list(arr + [root.val]))
    if root.left:
        sum_path(root.left, leftover - root.val, res, arr + [root.val])
        sum_path(root.left, leftover, res, [])
    if root.right:
        sum_path(root.right, leftover - root.val, res, arr + [root.val])
        sum_path(root.right, leftover, res, [])

if __name__ == '__main__':
    # import pdb
    # pdb.set_trace()
    lst = [3, 5, 9, 10, 1, 4, 7, 5, 6, 12, 8, 9]
    root = TreeNode.create_from_array(lst)
    res = []
    sum_path(root, 10, res, [])
    print '\n'.join([' '.join([str(s) for s in item]) for item in res])
    res = []
    sum_path(root, 23, res, [])
    print '\n'.join([' '.join([str(s) for s in item]) for item in res])
