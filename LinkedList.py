class LinkedList:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def print_self(self):
        p = self
        while p:
            print str(p.val) + ' ->',
            p = p.next

    @staticmethod
    def build_rec(arr):
        if not arr:
            return None
        else:
            head = LinkedList(arr[0])
            n = LinkedList.build(arr[1:])
            head.next = n
            return head

    @staticmethod
    def build_itr(arr):
        if arr:
            head = LinkedList(arr[0])
            p = head
            for i in arr[1:]:
                p.next = LinkedList(i)
                p = p.next
            return head
        else:
            return None

    def reverse_rec(self):
        if not self.next:
            return self
        else:
            p = self.next
            self.next = None
            head = p.reverse_rec()
            p.next = self
            return head

    def reverse_itr(self):
        dummy = LinkedList()
        p = self
        while p:
            tmp = p
            p = p.next
            tmp.next = dummy.next
            dummy.next = tmp
        return dummy.next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)

if __name__ == '__main__':
    arr = [i for i in xrange(1, 7)]
    head = LinkedList.build_itr(arr)
    head.print_self()
    head = head.reverse_itr()
    print
    head.print_self()
