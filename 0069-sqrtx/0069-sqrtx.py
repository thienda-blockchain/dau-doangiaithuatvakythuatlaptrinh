class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x
            
        trai = 1
        phai = x
        
        while trai <= phai:
            giua = (trai + phai) // 2
            binh_phuong = giua * giua
            
            if binh_phuong == x:
                return giua
            elif binh_phuong < x:
                trai = giua + 1
            else:
                phai = giua - 1
                
        # Khi vòng lặp kết thúc mà không tìm thấy căn chính xác,
        # con trỏ 'phai' sẽ tự động lùi về số nguyên nhỏ hơn gần nhất.
        # Đề bài yêu cầu "rounded down", nên 'phai' chính là đáp án hoàn hảo!
        return phai