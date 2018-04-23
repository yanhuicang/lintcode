import copy
import time
class DiceSum:
    # @param {int} n an integer
    # @return {tuple[]} a list of tuple(sum, probability)
    def diceSumInfo(self, n):
        # Write your code here
        dice = {}
        dice[n]  = [[n, 0, 0, 0, 0, 0]]
        for i in xrange(n + 1, 6 * n + 1):
            tmp_list = list()
            dice[i] = list()
            for dd in dice[i - 1]:
                for d in xrange(5):
                    tmp = copy.copy(dd)
                    if tmp[d] > 0:
                        tmp[d] = dd[d] - 1
                        tmp[d + 1] = dd[d + 1] + 1
                        tmp_list.append(tmp)
            for l in tmp_list:
                if l not in dice[i]:
                    dice[i].append(l)
            
        print dice

    def diceSum(self, n):
        if n == 1:
            return {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}
        d = self.diceSum(n - 1)
        result = dict()
        for k, v in d.items():
            for i in xrange(1, 7):
                result[k + i] = result.get(k + i, 0) + v
        return result 
print DiceSum().diceSum(3) 
