class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        gioi_han = len(candyType) // 2
        so_loai_keo_co_san = len(set(candyType))
        return min(gioi_han, so_loai_keo_co_san)