from TreeNode import TreeNode


class BSTreeNode(TreeNode):
    @staticmethod
    def create_from_array(array):
        if not all([array[i] <= array[i+1] for i in xrange(len(array) - 1)]):
            array.sort()
        return BSTreeNode.create_from_array_rec(array, 0, len(array)-1)

    @staticmethod
    def create_from_array_rec(array, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        node = BSTreeNode(array[mid])
        node.left = BSTreeNode.create_from_array_rec(array, start, mid-1)
        node.right = BSTreeNode.create_from_array_rec(array, mid+1, end)
        return node

    def insert(self, node):
        pass

    def delete(self, node):
        pass

    def find(self, val):
        if self.val == val:
            return self
        elif self.val < val:
            if self.right:
                return self.right.find(val)
        else:
            if self.left:
                return self.left.find(val)
