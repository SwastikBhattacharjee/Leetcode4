"""
Author: Swastik Bhattacharjee
Date: 17th February, 2023
Github: @SwastikBhattacharjee
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)

        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2] + nums[(len(nums) // 2) - 1]) / 2
        else:
            return nums[len(nums) // 2]
        
        
print(Solution().findMedianSortedArrays([1,2], [3,4]))
