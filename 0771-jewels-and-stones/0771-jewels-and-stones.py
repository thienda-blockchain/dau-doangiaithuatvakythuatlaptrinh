class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        da_quy = set(jewels)
        dem = 0
        for vien_da in stones:
            if vien_da in da_quy:
                dem += 1
        return dem 