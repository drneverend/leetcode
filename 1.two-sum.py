class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    for i in range(len(nums)):
      for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
          result = [i,j]
          break
    return result

if __name__ == "__main__":
  obj = Solution()
  print(obj.twoSum([3,3], 6))
  print(obj.twoSum([3,2,4], 6))
  print(obj.twoSum([3,2,4], 5))
  print(obj.twoSum([3,2,4,7], 7))
