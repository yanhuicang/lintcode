#!/usr/bin/env python
# -*-coding:utf-8 -*-

"""
@param N: The number of buses
@param route: The route of buses
@param A: Start bus station
@param B: End bus station
@return: Return the minimum transfer number
"""
def getMinTransferNumber(N, route, A, B):
    # Write your code here
    station = list()
    route0 = list()
    for i in xrange(N):
        if A in route[i]:
            route0.extend(route[i])
    station.append(route0)
    result = 1
    while B not in station[result - 1] and result <= len(route):
        print station
        tmp = list()
        for s in station[result - 1]:
            for i in xrange(N):
                if s in route[i]:
                    print route[i]
                    tmp.extend(route[i])
        station.append(tmp)
        result += 1
    if B in station[result - 1]
        return result
    return -1

if "__main__" == __name__:
    print getMinTransferNumber(2, [[0,1,2,3],[2,4,5,6]], 3, 4)
