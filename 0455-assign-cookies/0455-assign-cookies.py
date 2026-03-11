class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        em = 0
        banh = 0

        while em < len(g) and banh < len(s):
            if s[banh] >= g[em]:
                em += 1

            banh+=1

        return em 