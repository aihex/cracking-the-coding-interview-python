from TreeNode import TreeNode
import random


class BSTreeNode(TreeNode):
    @staticmethod
    def create_from_array(array):
        if not all([array[i] <= array[i+1] for i in xrange(len(array) - 1)]):
            array = sorted(array)
        return BSTreeNode.create_from_array_rec(array, 0, len(array)-1)

    @staticmethod
    def create_from_array_rec(array, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        node = BSTreeNode(array[mid])
        node.left = BSTreeNode.create_from_array_rec(array, start, mid-1)
        node.right = BSTreeNode.create_from_array_rec(array, mid+1, end)
        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node
        return node

    def insert(self, val):
        if val < self.val:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BSTreeNode(val)
                if self.left:
                    self.left.parent = self
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BSTreeNode(val)
                if self.right:
                    self.right.parent = self

    def delete(self, val):
        node = self.find(val)
        if not node:
            return None
        if node.left and node.right:
            tmp = node.right
            while tmp.left:
                tmp = tmp.left
            node.val = tmp.val
            return tmp.replace(self, tmp.right)
        elif node.left:
            return node.replace(self, node.left)
        elif node.right:
            return node.replace(self, node.right)
        else:
            return node.replace(self)

    def replace(self, root, node=None):
        if self == root:
            if node:
                node.parent = None
            return node
        else:
            if self.parent.left == self:
                self.parent.left = node
            else:
                self.parent.right = node
            if node:
                node.parent = self.parent
            return root

    def find(self, val):
        if self.val == val:
            return self
        elif self.val < val:
            if self.right:
                return self.right.find(val)
        else:
            if self.left:
                return self.left.find(val)

if __name__ == '__main__':
    array = [random.randint(0, 10000) for i in xrange(100)]
    # array = [1, 1, 42]
    print array
    # root1 = BSTreeNode.create_from_array(array)
    # root1.inorder_print()
    print
    root2 = BSTreeNode(array[0])
    for i in xrange(1, len(array)):
        root2.insert(array[i])
    root2.inorder_print()
    print '-----',
    root2.preorder_print()
    print
    for i in array[:]:
        print 'delete ' + str(i)
        root2 = root2.delete(i)
        if root2:
            root2.inorder_print()
            print '-----',
            root2.preorder_print()
            print
