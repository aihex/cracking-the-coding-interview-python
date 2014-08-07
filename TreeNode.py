class TreeNode:
  def __init__(self, val=0):
    self.val = val
    self.left = None
    self.right = None

  def inorderprint(self):
    print self.val,
    if self.left:
      self.left.inorderprint(),
    if self.right:
      self.right.inorderprint(),
