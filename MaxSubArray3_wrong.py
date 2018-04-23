#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
时间复杂度太高
"""
import sys
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxOneSubArray(self, nums):
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

    def maxSubArray(self, nums, k):
        if k == 1:
            return self.maxOneSubArray(nums)
        if k == 2:
            return self.maxTwoSubArrays(nums)
        if k > len(nums):
            return 0 - sys.maxint
        negative_count = 0
        # optimization
        max_k = list()
        min = 0 - sys.maxint
        result = 0
        for i in nums:
            if i < 0:
                negative_count += 1
            else:
                result += i
            if min < i:
                if len(max_k) == k:
                    for index in xrange(k):
                        if max_k[index] == min:
                            max_k.pop(index)
                min = i
                max_k.append(i)
        if negative_count < k and (len(nums) - negative_count) >= k:
            print "---"
            return result
        if (len(nums) - negative_count) <= k:
            return sum(max_k)
        result = 0 - sys.maxint
        for i in xrange(1, len(nums) - 1):
            left = self.maxOneSubArray(nums[:i])
            right = self.maxSubArray(nums[i:], k-1)
            if result < left + right:
                result = left + right
        return result

