#!/usr/bin/env python
# -*-coding:utf-8 -*-
import sys
class Solution():
    def maxSubArray(self, nums):
        """
        最大子数组, 返回最大和
        """
        result = nums[0]
        before = result
        for i in xrange(1, len(nums)):
            if before <= 0:
                if nums[i] > result:
                    result = nums[i]
                before = nums[i]
            else:
                if result < (nums[i] + before):
                    result = nums[i] + before
                before = nums[i] + before
                
        return result
       
    def maxSubArrayList(self, nums):
        """
        最大子数组, 返回中间结果
        """
        before = [nums[0]]
        result = [nums[0]]
        for i in xrange(1, len(nums)):
            if before[i - 1] <= 0:
                if nums[i] > result[i-1]:
                    result.append(nums[i])
                else:
                    result.append(result[i - 1])
                before.append(nums[i])
            else:
                r = nums[i] + before[i - 1]
                if result[i - 1]  < r:
                    result.append(r)
                else:
                    result.append(result[i - 1])
                before.append(r)

        return result

    def maxTwoSubArrays(self, nums):
        left = self.maxSubArrayList(nums)
        nums.reverse()
        right = self.maxSubArrayList(nums)
        right.reverse()
        result = left[0] + right[1]
        for l, r in zip(left[:-1], right[1:]):
            if result < l + r:
                result = l + r
        return result 
    
    def maxSubArrays(self, nums, k):
        if k == 1:
            return self.maxSubArray(nums)
        if k == 2:
            return self.maxTwoSubArrays(nums)
        if k > len(nums):
            return 0 - sys.maxint
        result = 0 - sys.maxint
        for i in xrange(1, len(nums) - 1):
            left = self.maxSubArray(nums[:i])
            right = self.maxSubArrays(nums, k-1)
            if result < left + right:
                result = left + right
        return result        

print Solution().maxSubArrays([1, 2, 3, -5, -1, 2, 3, -1, 0, 3, -2, -10, 1, 0, -1, 2, 3], 3)
        

