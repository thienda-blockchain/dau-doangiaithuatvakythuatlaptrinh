class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        check = {}
        for chu in t:
            check[chu] = check.get(chu, 0) + 1

        for chu in s:
            check[chu] -= 1

        for chu in check:
            if check[chu] > 0:
                return chu
