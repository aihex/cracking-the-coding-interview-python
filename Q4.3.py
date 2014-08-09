from TreeNode import TreeNode


def create_minimal_binary_tree(list_sort):
    if not list_sort:
        return None
    if len(list_sort) == 1:
        return TreeNode(list_sort[0])
    elif len(list_sort) == 2:
        root = TreeNode(list_sort[0])
        root.right = TreeNode(list_sort[1])
        return root
    else:
        half = len(list_sort) / 2
        root = TreeNode(list_sort[half])
        root.left = create_minimal_binary_tree(list_sort[0:half])
        root.right = create_minimal_binary_tree(list_sort[half+1:])
        return root

if __name__ == '__main__':
    list_sort = [1, 1, 2, 3, 3, 4, 4, 5, 7, 8, 9, 10]
    root = create_minimal_binary_tree(list_sort)
    root.inorder_print()
    print
    root.preorder_print()
