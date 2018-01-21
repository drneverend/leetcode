
def search_even_palindrome(s):
  if len(s) < 2:
    return ""
  else:
    i = 0
    maxlen = 0
    start = 0
    end = 0
    while i < len(s) - 1:
      if s[i] == s[i+1]:
        l = i
        r = i + 1
        while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
          l = l - 1
          r = r + 1
        curlen = r - l + 1
        if curlen > maxlen:
          maxlen = curlen
          start = l
          end = r + 1
      i = i + 1
    return s[start:end]

def search_odd_palindrome(s):
  if len(s) < 1:
    return ""
  elif len(s) == 1:
    return s
  elif len(s) == 2:
    return ""
  else:
    i = 1
    maxlen = 0
    start = 0
    end = 1
    while i < len(s) - 1:
      if s[i - 1] == s[i+1]:
        l = i - 1
        r = i + 1
        while l - 1 >= 0 and r + 1 < len(s) and s[l - 1] == s[r + 1]:
          l = l - 1
          r = r + 1
        curlen = r - l + 1
        if curlen > maxlen:
          maxlen = curlen
          start = l
          end = r + 1
      i = i + 1
    return s[start:end]

class Solution(object):
  def longestPalindrome(self, s):
    """
    :type s: str
    :rtype: str
    """
    s1 = search_even_palindrome(s)
    s2 = search_odd_palindrome(s)
    if len(s1) < len(s2):
      return s2
    else:
      return s1



if __name__ == "__main__":
  obj = Solution()
  s = ""
  print("%s - %s" % (s, obj.longestPalindrome(s)))
  s = "a"
  print("%s - %s" % (s, obj.longestPalindrome(s)))
  s = "aa"
  print("%s - %s" % (s, obj.longestPalindrome(s)))
  s = "ab"
  print("%s - %s" % (s, obj.longestPalindrome(s)))
  s = "aba"
  print("%s - %s" % (s, obj.longestPalindrome(s)))
  s = "baba"
  print("%s - %s" % (s, obj.longestPalindrome(s)))
  s = "abab"
  print("%s - %s" % (s, obj.longestPalindrome(s)))
  s = "abababbababa"
  print("%s - %s" % (s, obj.longestPalindrome(s)))
