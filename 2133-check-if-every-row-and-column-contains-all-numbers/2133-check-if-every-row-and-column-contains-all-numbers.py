class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
       # n là kích thước của ma trận n x n
        n = len(matrix)
        
        # Kiểm tra từng hàng
        for hang in matrix:
            # Nếu độ dài của set khác n, nghĩa là hàng đó có số bị trùng hoặc thiếu
            if len(set(hang)) != n:
                return False
        
        # Kiểm tra từng cột
        # zip(*matrix) là để xoay ma trận (chuyển hàng thành cột)
        for cot in zip(*matrix):
            if len(set(cot)) != n:
                return False
                
        return True