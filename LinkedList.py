class LinkedList:
  def __init__(self, val = 0):
    self.val = val
    self.next = None

  def selfprint(self):
    p = self
    while p != None:
      print str(p.val) + ' ->',
      p = p.next
