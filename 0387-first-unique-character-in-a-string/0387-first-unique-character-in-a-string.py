class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        check = {}
        for i in range (len(s)):
            chu_cai = s[i]
            check[chu_cai] = check.get(chu_cai, 0) + 1

        for i in range (len(s)):
            chu_cai = s[i]
            if check[chu_cai] == 1:
                return i

        return -1

