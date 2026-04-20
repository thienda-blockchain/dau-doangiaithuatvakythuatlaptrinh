class Solution(object):
    def minimumCost(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.sort(reverse=True)

        tong = 0
        for i in range(len(cost)):
            if (i+1) % 3 != 0:
                tong += cost[i]
        return tong