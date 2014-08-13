class MyQueue():
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, n):
        self.stack_in.append(n)

    def pop(self):
        if len(self.stack_out) == 0:
            if len(self.stack_in) == 0:
                return None
            else:
                while len(self.stack_in):
                    self.stack_out.append(self.stack_in.pop())
                return self.stack_out.pop()
        else:
            return self.stack_out.pop()

if __name__ == '__main__':
    mq = MyQueue()
    print mq.pop()
    for i in xrange(10):
        mq.push(i)
    print mq.stack_in
    print mq.stack_out
    for i in xrange(5):
        print mq.pop()
    print mq.stack_in
    print mq.stack_out
    for i in xrange(5):
        mq.push(i+10)
    print mq.stack_in
    print mq.stack_out
    for i in xrange(10):
        print mq.pop()
    print mq.stack_in
    print mq.stack_out
