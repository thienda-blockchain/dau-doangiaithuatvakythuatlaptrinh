class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        so_dat_lien = 0
        so_canh_lien_ke = 0
        
        so_hang = len(grid)
        so_cot = len(grid[0])
        
        # Quét radar toàn bộ bản đồ
        for r in range(so_hang):
            for c in range(so_cot):
                
                # Nếu phát hiện đất liền
                if grid[r][c] == 1:
                    so_dat_lien += 1
                    
                    # Kiểm tra xem có đất liền dính sát ở BÊN PHẢI không?
                    if c < so_cot - 1 and grid[r][c + 1] == 1:
                        so_canh_lien_ke += 1
                        
                    # Kiểm tra xem có đất liền dính sát ở BÊN DƯỚI không?
                    if r < so_hang - 1 and grid[r + 1][c] == 1:
                        so_canh_lien_ke += 1
                        
        # CÔNG THỨC VÀNG:
        # Mỗi ô đất cho 4 cạnh viền. 
        # Cứ 2 ô đất dính nhau thì mất đi 2 cạnh (do bị che khuất ở giữa)
        return so_dat_lien * 4 - so_canh_lien_ke * 2