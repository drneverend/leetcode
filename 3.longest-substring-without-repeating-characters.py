
def nextstart(s, start, stop):
  uniq = set(s[start: stop])
  findduplicate = False
  while stop < len(s):
    if s[stop] in uniq:
      findduplicate = True
      stop = stop + 1
      break
    else:
      uniq.add(s[stop])
      stop = stop + 1
  if findduplicate:
    while s[start] != s[stop - 1]:
      start = start + 1
  else:
    stop = stop + 1
  return start + 1, stop

class Solution(object):
  def lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) < 1 :
      return 0
    elif len(s) == 1:
      return 1
    else:
      maxlength = 1
      start = 0
      stop = 1
      while stop < len(s):
        start1, stop1 = nextstart(s, start, stop)
        l = stop1 - start - 1
        if l > maxlength:
          maxlength = l
        start = start1
        stop = stop1
      return maxlength

if __name__ == "__main__":
  obj = Solution()
  s = ""
  print("%s - %d" % (s, obj.lengthOfLongestSubstring(s)))
  s = "a"
  print("%s - %d" % (s, obj.lengthOfLongestSubstring(s)))
  s = "hello"
  print("%s - %d" % (s, obj.lengthOfLongestSubstring(s)))
  s = "bbbbbb"
  print("%s - %d" % (s, obj.lengthOfLongestSubstring(s)))
  s = "abcabcbb"
  print("%s - %d" % (s, obj.lengthOfLongestSubstring(s)))
  s = "pwwkew"
  print("%s - %d" % (s, obj.lengthOfLongestSubstring(s)))
  s = "ckclybxyyqsqieccych"
  print("%s - %d" % (s, obj.lengthOfLongestSubstring(s)))
