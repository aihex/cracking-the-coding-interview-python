import LinkedList
from LinkedList import LinkedList


def find_nth_to_last(head, n):
    dummy = LinkedList()
    dummy.next = head
    p = dummy
    while n > 0 and p.next:
        p = p.next
        n -= 1

    pp = dummy
    while pp.next and p.next:
        pp = pp.next
        p = p.next
    return pp.next

if __name__ == '__main__':
    n1 = LinkedList(1)
    n2 = LinkedList(2)
    n3 = LinkedList(3)

    n1.next = n2
    n2.next = n3

    print find_nth_to_last(n1, 0)
    print find_nth_to_last(n1, 1).val
    print find_nth_to_last(n1, 2).val
    print find_nth_to_last(n1, 3).val
    print find_nth_to_last(n1, 4).val
