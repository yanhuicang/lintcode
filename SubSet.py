import copy

class SubSet(object):
    def __init__(self):
        pass    
    
    def subsets(self, nums):
        # write your code here
        if len(nums) == 0:
            return [[]] 
        s1 = self.subsets(nums[:-1])
        result = copy.deepcopy(s1)
        for i in s1:
            i.append(nums[-1])
            result.append(i)
        return result

print SubSet().subsets([0, 1])
