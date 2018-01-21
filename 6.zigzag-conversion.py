
def reorder(s, n):
  maxoffset = (n - 1) * 2
  offsets = [maxoffset, 0]
  indices = []
  for i in range(n):
    pos = i
    offsetidx = 0
    while pos < len(s):
      indices.append(pos)
      offset = offsets[offsetidx]
      offsetidx = offsetidx + 1
      if offsetidx >= 2:
        offsetidx = 0
      if offset == 0:
        offset = maxoffset
      pos = pos + offset

    offsets[0] = offsets[0] - 2
    offsets[1] = offsets[1] + 2
  
  result = ""
  for i in indices:
    result = result + s[i]
  return result
  
  
class Solution(object):
  def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if len(s) <= numRows:
      return s
    elif numRows == 1:
      return s
    else:
      return reorder(s, numRows)


if __name__ == "__main__":
  obj = Solution()
  s = "PAYPALISHIRING"
  n = 3
  print("%s, %d - %s" % (s, n, obj.convert(s, n)))
  s = "abcdefghijklmnopqrst"
  n = 4
  print("%s, %d - %s" % (s, n, obj.convert(s, n)))
