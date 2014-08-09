class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def inorder_print(self):
        print self.val,
        if self.left:
            self.left.inorder_print(),
        if self.right:
            self.right.inorder_print(),

    def preorder_print(self):
        if self.left:
            self.left.preorder_print()
        print self.val,
        if self.right:
            self.right.preorder_print()
