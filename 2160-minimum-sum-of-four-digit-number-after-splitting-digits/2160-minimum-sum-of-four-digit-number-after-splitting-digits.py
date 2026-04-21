class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
    
        chuoi = sorted(str(num))
        so_1 = int(chuoi[0] + chuoi[2])
        so_2 = int(chuoi[1] + chuoi[3])

        return so_1 + so_2