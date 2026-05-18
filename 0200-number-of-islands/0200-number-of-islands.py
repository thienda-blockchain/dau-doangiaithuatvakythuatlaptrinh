class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
            
        so_luong_dao = 0
        so_hang = len(grid)
        so_cot = len(grid[0])
        
        # Hàm đệ quy DFS dùng để "Đánh chìm" hòn đảo
        def danh_chim_dao(r, c):
            # CHỐT CHẶN: 
            # 1. Rơi ra ngoài ranh giới bản đồ (trên, dưới, trái, phải)
            # 2. Hoặc rơi vào vùng nước ('0')
            if r < 0 or c < 0 or r >= so_hang or c >= so_cot or grid[r][c] == '0':
                return
            
            # Nếu đang đứng trên đất liền ('1'), ngay lập tức "đánh chìm" nó thành nước ('0')
            # Việc này giúp ta không bao giờ đi lại vào ô này nữa
            grid[r][c] = '0'
            
            # Sai lính lan ra 4 hướng để đánh chìm tiếp các phần đất liền nối với nó
            danh_chim_dao(r - 1, c) # Lên trên
            danh_chim_dao(r + 1, c) # Xuống dưới
            danh_chim_dao(r, c - 1) # Sang trái
            danh_chim_dao(r, c + 1) # Sang phải

        # Quét radar toàn bộ bản đồ từ trên xuống dưới, từ trái sang phải
        for r in range(so_hang):
            for c in range(so_cot):
                # Nếu radar phát hiện đất liền chưa bị chìm
                if grid[r][c] == '1':
                    # Ghi nhận đây là một hòn đảo mới
                    so_luong_dao += 1
                    
                    # Gọi trực thăng đến "đánh chìm" toàn bộ hòn đảo này
                    danh_chim_dao(r, c)
                    
        return so_luong_dao