class LinkedList:
    def __init__(self, val=0):
        self.val = val
        self.next = None

    def print_self(self):
        p = self
        while p:
            print str(p.val) + ' ->',
            p = p.next

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)
