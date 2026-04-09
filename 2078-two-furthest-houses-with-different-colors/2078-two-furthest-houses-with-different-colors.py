class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        n = len(colors)
        max_dist = 0
        
        # Chiến thuật: Một trong hai nhà chắc chắn phải nằm ở đầu hoặc cuối dãy
        
        # Trường hợp 1: So sánh nhà đầu tiên (index 0) với các nhà từ cuối về
        for j in range(n - 1, 0, -1):
            if colors[j] != colors[0]:
                max_dist = max(max_dist, j)
                break # Tìm thấy nhà xa nhất khác màu đầu tiên thì dừng luôn
                
        # Trường hợp 2: So sánh nhà cuối cùng (index n-1) với các nhà từ đầu tới
        for i in range(0, n - 1):
            if colors[i] != colors[n - 1]:
                max_dist = max(max_dist, n - 1 - i)
                break # Tìm thấy nhà xa nhất khác màu cuối cùng thì dừng luôn
                
        return max_dist