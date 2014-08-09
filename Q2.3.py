from LinkedList import LinkedList


def remove(node):
    if node:
        if node.next:
            node.val = node.next.val
            node.next = node.next.next
        else:
            pass  # cannot handle using this method

if __name__ == '__main__':
    n1 = LinkedList(1)
    n2 = LinkedList(2)
    n3 = LinkedList(3)

    n1.next = n2
    n2.next = n3

    remove(n3)

    n1.selfprint()
