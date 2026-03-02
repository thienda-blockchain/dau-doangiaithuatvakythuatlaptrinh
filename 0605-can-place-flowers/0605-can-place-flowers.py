class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(flowerbed)):
            if n <= 0:
                return True

            if flowerbed[i] == 0:
                # Kiểm tra bên trái (ô đầu tiên hoặc ô bên trái là 0)
                trai_trong = (i == 0) or (flowerbed[i - 1] == 0)
                
                # Kiểm tra bên phải (ô cuối cùng hoặc ô bên phải là 0)
                phai_trong = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                
                if trai_trong and phai_trong:
                    flowerbed[i] = 1 # Đánh dấu đã trồng
                    n -= 1 # Giảm số cây còn lại cần trồng
                    
        return n <= 0
                