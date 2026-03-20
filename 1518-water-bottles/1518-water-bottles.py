class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        tong_uong = numBottles
        vo_trong = numBottles
        while vo_trong >= numExchange:
            chai_moi = vo_trong // numExchange
            vo_du = vo_trong % numExchange
            tong_uong += chai_moi
            vo_trong = chai_moi + vo_du
        return tong_uong