#!/usr/bin/env python
# -*-coding:utf-8 -*-
class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        if n == 0:
            return 0
        factor2 = 0
        factor3 = 0
        factor5 = 0
        ugly_nums = list()
        ugly_nums.append(1)
        i = 1
        while i < n:
            ugly_num = min(ugly_nums[factor2] * 2, ugly_nums[factor3] * 3, ugly_nums[factor5] * 5)
            if ugly_num == ugly_nums[factor2] * 2:
                factor2 += 1
            elif ugly_num == ugly_nums[factor3] * 3:
                factor3 += 1
            else:
                factor5 += 1
            if ugly_num not in ugly_nums:
                ugly_nums.append(ugly_num)
                i += 1
        return ugly_nums[-1]

            
    def nthUglyNumberError(self, n):
        # write your code here
        base = [1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16, 18, 20, 24, 25, 27]
        if n <= len(base):
            return base[n-1]
        cal_list = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (2, 0, 0), (0, 0, 1), \
                    (1, 1, 0), (3, 0, 0), (0, 2, 0), (1, 0, 1), (2, 1, 0), \
                    (0, 1, 1), (4, 0, 0), (1, 2, 0), (2, 0, 1), (3, 1, 0), \
                    (0, 0, 2), (0, 3, 0)] 
        cal_dict = {(0, 0, 0):1, (1, 0, 0):2, (0, 1, 0):3, (2, 0, 0):4, (0, 0, 1):5, \
                    (1, 1, 0):6, (3, 0, 0):7, (0, 2, 0):8, (1, 0, 1):9, (2, 1, 0):10, \
                    (0, 1, 1):11, (4, 0, 0):12, (1, 2, 0):13, (2, 0, 1):14, (3, 1, 0):15, \
                    (0, 0, 2):16, (0, 3, 0):0}
        [4, 3, 2]
        m = self.nthUglyNumber(n - 1)
        factors = self.getFactors(m)
        print factors
        minn = min(factors)
        c = (factors[0] - minn, factors[1] - minn, factors[2] - minn)
        if (0, 3, 0) == c:
            b = minn + 1
        else:
            b = minn
        power = cal_list[cal_dict[c]]
        return 
    
    def getFactors(self, n):
        a = 0
        b = 0
        c = 0
        while n != 1:
            if n % 2 == 0:
                n = n / 2
                a += 1
                continue
            
            if n % 3 == 0:
                n = n / 3
                b += 1
                continue
            
            if n % 5 == 0:
                n = n / 5
                c += 1
                continue
        return (a, b, c)
 
if "__main__" == __name__:
    S = Solution()
    #print S.getFactors(60)
    print S.nthUglyNumber(20)
