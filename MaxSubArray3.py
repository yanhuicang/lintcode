#!/usr/bin/env python
# -*-coding:utf-8 -*-

import sys
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer denote to find k non-overlapping subarrays
    @return: An integer denote the sum of max k non-overlapping subarrays
    """
    def maxSubArray(self, nums, k):
        # write your code here
        minint = 0 - sys.maxint
        tmp1 = list()
        tmp2 = list()
        n = len(nums)
        if n < k:
            return minint
        for i in xrange(k + 1):
            tmp1.append([minint] * (n + 1))
            tmp2.append([minint] * (n + 1))
        for i in xrange(1, k + 1):
            for j in xrange(i, n + 1):
                tmp = max(tmp1[i][j-1], tmp2[i-1][j-1])
                if tmp == minint:
                    tmp = 0
                if tmp < 0 and i == 1:
                    tmp1[i][j] = nums[j-1]
                else:
                    tmp1[i][j] = tmp + nums[j-1]
                if i == j:
                    tmp2[i][j] = tmp1[i][j]
                else:
                    tmp2[i][j] = max(tmp2[i][j-1], tmp1[i][j])
        self.ppp(tmp1)
        print "----"
        self.ppp(tmp2)
        return tmp2[k][n] 
                
    def ppp(self, tmp):
        for i in tmp:
            print str(i).replace("-9223372036854775807", "").replace(" ", "\t")
print Solution().maxSubArray([-1,4,-2,3,-2,3], 2)
