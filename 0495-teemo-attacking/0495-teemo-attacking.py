class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        
        tong_thoi_gian = 0
        n = len(timeSeries)
        
        for i in range(n - 1):
            khoang_cach = timeSeries[i+1] - timeSeries[i]
            if khoang_cach < duration:
                tong_thoi_gian += khoang_cach
            else:
                tong_thoi_gian += duration
        tong_thoi_gian += duration
        
        return tong_thoi_gian