import LinkedList
from LinkedList import LinkedList
def removedulicate(head):
  s = set()
  dummy = head
  p = head
  while p != None and p.next != None:
    print p.next.val
    if p.next.val in s:
      p.next = p.next.next
    else:
      s.add(p.next.val)
      p = p.next

if __name__ == '__main__':
  n1 = LinkedList(1)
  n2 = LinkedList(1)
  n3 = LinkedList(2)
  n4 = LinkedList(1)
  n1.next = n2
  n2.next = n3
  n3.next = n4
  dummy = LinkedList(0)
  dummy.next = n1
  removedulicate(dummy)
  dummy.selfprint()
