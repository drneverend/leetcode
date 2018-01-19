# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def listtoval(h):
  v = 0
  t = 1
  while h != None:
    v = v + t * h.val
    h = h.next
    t = t * 10
  return v

def valtolist(v):
  head = None
  last = None
  while v > 0:
    r = v % 10
    if head == None:
      head = ListNode(r)
      head.next = None
      last = head
    else:
      last.next = ListNode(r)
      last = last.next
      last.next = None
    v = int(v / 10)
  if head == None:
    head = ListNode(0)
    head.next = None
  return head

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    v1 = listtoval(l1)
    v2 = listtoval(l2)
    r = v1 + v2

    return valtolist(r)


