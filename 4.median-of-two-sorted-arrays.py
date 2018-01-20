
def median1array(a):
  n = len(a)
  if n < 1:
    return 0
  if n % 2 == 0:
    return (a[n / 2] + a[n / 2 - 1] ) / 2.0
  else:
    return a[n / 2]

def median2array(a1, a2):
  n = len(a1) + len(a2)
  i1 = 0
  i2 = 0
  l = n / 2
  while i1 + i2 < l:
    if i2 >= len(a2) :
      i1 = i1 + 1
    elif i1 >= len(a1):
      i2 = i2 + 1
    elif a1[i1] < a2[i2]:
      i1 = i1 + 1
    else:
      i2 = i2 + 1

  if n % 2 == 0:
    if i1 == 0:
      v1 = a2[i2 - 1]
    elif i2 == 0:
      v1 = a1[i1 - 1]
    else:
      v1 = max(a1[i1 - 1], a2[i2 - 1])
    if i1 >= len(a1):
      v2 = a2[i2]
    elif i2 >= len(a2):
      v2 = a1[i1]
    else:
      v2 = min(a1[i1], a2[i2])
    return (v1 + v2) / 2.0
  else:
    if i1 >= len(a1):
      v2 = a2[i2]
    elif i2 >= len(a2):
      v2 = a1[i1]
    else:
      v2 = min(a1[i1], a2[i2])
    return v2

class Solution(object):
  def findMedianSortedArrays(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    if nums1 == None or len(nums1) < 1:
      return median1array(nums2)
    if nums2 == None or len(nums2) < 1:
      return median1array(nums1)
    return median2array(nums1, nums2)

if __name__ == "__main__":
  obj = Solution()
  nums1 = [1,2,3]
  nums2 = [4,5,6]
  print("%s - %s = %f" % (str(nums1), str(nums2), median2array(nums1, nums2)))
  nums1 = [1,3]
  nums2 = [2]
  print("%s - %s = %f" % (str(nums1), str(nums2), median2array(nums1, nums2)))
  nums1 = [1,3]
  nums2 = [2,4]
  print("%s - %s = %f" % (str(nums1), str(nums2), median2array(nums1, nums2)))
  nums1 = [1,3]
  nums2 = []
  print("%s - %s = %f" % (str(nums1), str(nums2), median2array(nums1, nums2)))
  nums1 = []
  nums2 = [1]
  print("%s - %s = %f" % (str(nums1), str(nums2), median2array(nums1, nums2)))
  nums1 = [1,2,8]
  nums2 = [4,5,6]
  print("%s - %s = %f" % (str(nums1), str(nums2), median2array(nums1, nums2)))
