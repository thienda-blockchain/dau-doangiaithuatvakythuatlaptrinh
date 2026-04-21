class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        
        # Vòng lặp 1: Chọn vị trí i (từ đầu mảng đến cuối)
        for i in range(n):
            # Vòng lặp 2: Chọn vị trí j (luôn bắt đầu từ ngay sau i)
            # Điều này đảm bảo i < j 
            for j in range(i + 1, n):
                
                # Kiểm tra 2 điều kiện:
                # 1. Hai giá trị phải bằng nhau
                # 2. (i * j) chia hết cho k
                if nums[i] == nums[j] and (i * j) % k == 0:
                    count += 1
                    
        return count