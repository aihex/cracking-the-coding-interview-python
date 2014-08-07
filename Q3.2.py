class MinStack:
    def __init__(self):
        self.list_data = []
        self.list_min = []

    def min_stack(self):
        if len(self.list_min) == 0:
            return None
        return self.list_min[-1]

    def push(self, n):
        self.list_data.append(n)
        if len(self.list_data) == 1:
            self.list_min.append(n)
        elif n <= self.min_stack():
            self.list_min.append(n)

    def pop(self):
        if len(self.list_data) == 0:
            return None
        n = self.list_data.pop()
        if n <= self.min_stack():
            self.list_min.pop()
        return n

if __name__ == '__main__':
    stack = MinStack()
    for i in xrange(0, 100):
        stack.push(i)
    for i in xrange(0, 50):
        stack.pop()
    print stack.min_stack()
    print stack.list_min

    stack1 = MinStack()
    for i in xrange(100, 0, -1):
        stack1.push(i)
    for i in xrange(0, 50):
        stack1.pop()
    # print stack1.list_data
    print stack1.min_stack()
    print stack1.list_min
