class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for chu in s:
            if "ba" in s:
                return False
        return True

        