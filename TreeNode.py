import random
from rand import rand_perm
import time


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    @staticmethod
    def create_from_array(array):
        return TreeNode.create_from_array_rec(array, 0, len(array)-1)

    @staticmethod
    def create_from_array_rec(array, start, end):
        if start > end:
            return None
        mid = (start + end) >> 1
        node = TreeNode(array[mid])
        node.left = TreeNode.create_from_array_rec(array, start, mid-1)
        node.right = TreeNode.create_from_array_rec(array, mid+1, end)
        if node.left:
            node.left.parent = node
        if node.right:
            node.right.parent = node
        return node

    def inorder_print(self):
        if self.left:
            self.left.inorder_print()
        print self.val,
        if self.right:
            self.right.inorder_print()

    def preorder_print(self):
        print self.val,
        if self.left:
            self.left.preorder_print(),
        if self.right:
            self.right.preorder_print(),

    def postorder_print(self):
        if self.left:
            self.left.postorder_print()
        if self.right:
            self.right.postorder_print()
        print self.val,

    def inorder_print_advanced(self):
        # cur = self
        # while cur:
        #     if not cur.left:
        #         print cur.val,
        #         cur = cur.right
        #     else:
        #         # find predecessor
        #         tmp = cur.left
        #         while tmp.right and tmp.right != cur:
        #             tmp = tmp.right
        #         if not tmp.right:
        #             tmp.right = cur
        #             cur = cur.left
        #         else:
        #             tmp.right = None
        #             print cur.val,
        #             cur = cur.right
        res = self.inorder_itr()
        print ' '.join([str(cur.val) for cur in res])

    def preorder_print_advanced(self):
        # cur = self
        # while cur:
        #     if not cur.left:
        #         print cur.val,
        #         cur = cur.right
        #     else:
        #         tmp = cur.left
        #         while tmp.right and tmp.right != cur:
        #             tmp = tmp.right
        #         if not tmp.right:
        #             tmp.right = cur
        #             print cur.val,
        #             cur = cur.left
        #         else:
        #             tmp.right = None
        #             cur = cur.right
        res = self.preorder_itr()
        # print res
        print ' '.join([str(cur.val) for cur in res])

    def postorder_print_advanced(self):
        dummy = TreeNode()
        dummy.left = self
        cur = dummy
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = cur
                    cur = cur.left
                else:
                    # reversely print from cur.left to tmp
                    cur.left.reverse_print(tmp)
                    tmp.right = None
                    cur = cur.right

    def reverse_print(self, to):
        cur = self
        res = []
        while cur != to:
            res.append(cur)
            cur = cur.right
        res.append(to)
        while res:
            print res.pop().val,

    def preorder_itr(self):
        res = []
        cur = self
        while cur:
            if not cur.left:
                res.append(cur)
                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    res.append(cur)
                    tmp.right = cur
                    cur = cur.left
                else:
                    tmp.right = None
                    cur = cur.right
        return res

    def inorder_itr(self):
        cur = self
        res = []
        while cur:
            if not cur.left:
                res.append(cur)
                cur = cur.right
            else:
                tmp = cur.left
                while tmp.right and tmp.right != cur:
                    tmp = tmp.right
                if not tmp.right:
                    tmp.right = cur
                    cur = cur.left
                else:
                    res.append(cur)
                    tmp.right = None
                    cur = cur.right
        return res

    @staticmethod
    def build_from_in_pre_order(in_traversal, pre_traversal):
        return TreeNode.build_from_in_pre_order_rec(in_traversal, pre_traversal, 0, len(in_traversal)-1, 0, len(pre_traversal)-1)

    @staticmethod
    def build_from_in_pre_order_rec(in_traversal, pre_traversal, s_i, e_i, s_p, e_p):
        if s_i == e_i:
            return TreeNode(in_traversal[s_i])
        elif s_i > e_i:
            return None
        else:
            mid = in_traversal[s_i:e_i+1].index(pre_traversal[s_p]) + s_i
            root = TreeNode(pre_traversal[s_p])
            root.left = TreeNode.build_from_in_pre_order_rec(in_traversal, pre_traversal, s_i, mid-1, s_p+1, s_p + 1 + ((mid-1)-s_i))
            root.right = TreeNode.build_from_in_pre_order_rec(in_traversal, pre_traversal, mid+1, e_i, e_p-(e_i-(mid+1)), e_p)
        return root

    @staticmethod
    def build_from_in_pre_order_fast(in_traversal, pre_traversal, idx_map):
        return TreeNode.build_from_in_pre_order_fast_rec(in_traversal, pre_traversal, idx_map, 0, len(in_traversal)-1, 0, len(pre_traversal)-1)

    @staticmethod
    def build_from_in_pre_order_fast_rec(in_traversal, pre_traversal, idx_map, s_i, e_i, s_p, e_p):
        if s_i > e_i:
            return None
        elif s_i == e_i:
            return TreeNode(in_traversal[s_i])
        else:
            mid = idx_map[pre_traversal[s_p]]
            root = TreeNode(pre_traversal[s_p])
            root.left = TreeNode.build_from_in_pre_order_fast_rec(in_traversal, pre_traversal, idx_map, s_i, mid-1, s_p+1, s_p+1+(mid-1-s_i))
            root.right = TreeNode.build_from_in_pre_order_fast_rec(in_traversal, pre_traversal, idx_map, mid+1, e_i, e_p-(e_i-(mid+1)), e_p)
            return root

    @staticmethod
    def is_identical_itr(root_1, root_2):
        q_1 = [root_1]
        q_2 = [root_2]
        while q_1 and q_2:
            cur_1 = q_1.pop(0)
            cur_2 = q_2.pop(0)
            if cur_1 == cur_2 is None:
                return True
            elif cur_1 is None or cur_2 is None:
                return False
            if cur_1.val != cur_2.val:
                return False
            if cur_1.left:
                q_1.append(cur_1.left)
            if cur_1.right:
                q_1.append(cur_1.right)
            if cur_2.left:
                q_2.append(cur_2.left)
            if cur_2.right:
                q_2.append(cur_2.right)
        if len(q_1) == len(q_2) == 0:
            return True
        else:
            return False

    @staticmethod
    def is_identical(root_1, root_2):
        if root_1 is not None and root_2 is not None:
            if root_1.val == root_2.val:
                return TreeNode.is_identical(root_1.left, root_2.left) and TreeNode. is_identical(root_1.right, root_2.right)
            else:
                return False
        elif root_1 is not None or root_2 is not None:
            return False
        else:
            return True

    def clone(self):
        root = TreeNode(self.val)
        if self.left:
            root.left = self.left.clone()
        if self.right:
            root.right = self.right.clone()
        return root

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


if __name__ == '__main__':
    # array = [random.randint(0, 10000) for i in xrange(20)]
    # array = [1, 1, 42]
    array = [i for i in xrange(1, 500000)]
    rand_perm(array)
    # print array
    root1 = TreeNode.create_from_array(array)
    # root1.inorder_print()
    # print '-----',
    # root1.preorder_print()
    # print
    # root2 = root1.clone()
    # print TreeNode.is_identical(root1, root2)
    # root2.inorder_print()
    # print '-----',
    # root2.preorder_print()
    # print
    # root2.inorder_print_advanced()
    # print '-----',
    # root2.preorder_print_advanced()
    # print
    # root2.postorder_print()
    # print
    # root2.postorder_print_advanced()
    in_traversal = [cur.val for cur in root1.inorder_itr()]
    pre_traversal = [cur.val for cur in root1.preorder_itr()]
    t_1 = time.time()
    root3 = TreeNode.build_from_in_pre_order(in_traversal, pre_traversal)
    print time.time() - t_1
    # print TreeNode.is_identical(root1, root3)
    # root3.inorder_print()
    # print '-----',
    # root3.preorder_print()
    # print
    # idx_map = {}
    idx_map = [0 for i in xrange(max(in_traversal)+1)]
    # for i in pre_traversal:
    #     idx_map[i] = in_traversal.index(i)
    for i in xrange(len(in_traversal)):
        idx_map[in_traversal[i]] = i
    t_2 = time.time()
    root4 = TreeNode.build_from_in_pre_order_fast(in_traversal, pre_traversal, idx_map)
    print time.time() - t_2
    print TreeNode.is_identical(root3, root4)
    # root4.inorder_print()
    # print '-----',
    # root4.preorder_print()
    # print
