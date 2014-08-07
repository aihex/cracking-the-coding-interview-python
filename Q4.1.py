from TreeNode import TreeNode

def is_balanced(root):
  return is_balanced_rec(root, TreeNode())

def is_balanced_rec(node, tmp):

  if node == None:
    return True

  tmp_left = TreeNode();
  tmp_right = TreeNode();

  is_balanced_l = is_balanced_rec(node.left, tmp_left)
  is_balanced_r = is_balanced_rec(node.right, tmp_right)

  tmp.val = max(tmp_left.val, tmp_right.val) + 1

  # depends on how "balaned" is defined
  # tmp.val = min(tmp_left.val, tmp_right.val) + 1

  return is_balanced_l and is_balanced_r and abs(tmp_left.val - tmp_right.val) <= 1



if __name__ == '__main__':
  n1 = TreeNode(1)
  n2 = TreeNode(2)
  n3 = TreeNode(3)
  n4 = TreeNode(4)
  n5 = TreeNode(5)

  n1.left = n2
  n1.right = n3
  n2.left = n4
  n4.right = n5
  n1.inorderprint()

  print is_balanced(n1)
