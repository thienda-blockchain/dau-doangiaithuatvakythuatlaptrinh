class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        new_heights = sorted(heights)
        dem = 0
        for i in range(len(new_heights)):
            if heights[i] != new_heights[i]:
                dem += 1
        return dem