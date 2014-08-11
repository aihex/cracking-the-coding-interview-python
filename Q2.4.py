from LinkedList import LinkedList


def add_link(head1, head2):
    carry = 0
    dummy1 = LinkedList()
    dummy2 = LinkedList()
    dummy1.next = head1
    dummy2.next = head2
    p1 = dummy1
    p2 = dummy2
    while p1.next and p2.next:
        carry += p1.next.val + p2.next.val
        p1.next.val = carry % 10
        carry /= 10
        p1 = p1.next
        p2 = p2.next

    while p1.next:
        carry += p1.next.val
        p1.next.val = carry % 10
        carry /= 10
        p1 = p1.next
    while p2.next:
        carry += p2.next.val
        p1.next = LinkedList(carry % 10)
        carry /= 10
        p1 = p1.next
        p2 = p2.next
    if carry:
        p1.next = LinkedList(carry)

    return dummy1.next


if __name__ == '__main__':
    p11 = LinkedList(8)
    p21 = LinkedList(9)
    p22 = LinkedList(9)
    p23 = LinkedList(9)
    p21.next = p22
    p22.next = p23

    add_link(p11, p21).print_self()
