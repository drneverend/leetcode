
def value_list(x):
  result = []
  while x > 0:
    result.append(x % 10)
    x = x / 10
  return result

def list_value(l):
  v = 0
  for lv in l:
    v = v * 10
    v = lv + v
  return v

def revert(x):
  l = value_list(x)
  return list_value(l)

class Solution(object):
  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x >= -9 and x <= 9:
      return x
    elif x > 0:
      r = revert(x)
      if r > 65536 * 32768:
        r = 0
      return r
    else:
      r = -revert(-x)
      if r <= (-65536 * 32768 + 1):
        r = 0
      return r

if __name__ == "__main__":
  obj = Solution()
  v = 0
  print("%d ~ %d" % (v, obj.reverse(v)) )
  v = 3
  print("%d ~ %d" % (v, obj.reverse(v)) )
  v = -10
  print("%d ~ %d" % (v, obj.reverse(v)) )
  v = -1
  print("%d ~ %d" % (v, obj.reverse(v)) )
  v = 123
  print("%d ~ %d" % (v, obj.reverse(v)) )
