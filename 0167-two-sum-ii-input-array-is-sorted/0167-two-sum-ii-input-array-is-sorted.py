class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
       # Đặt 2 con trỏ ở hai đầu của mảng
        trai = 0
        phai = len(numbers) - 1
        
        # Áp dụng chính xác vòng lặp mà bạn đã chọn ở bài 4Sum
        while trai < phai:
            tong = numbers[trai] + numbers[phai]
            
            if tong == target:
                # Đề bài yêu cầu chỉ số bắt đầu từ 1 (1-indexed) thay vì 0
                # Nên ta phải cộng thêm 1 vào kết quả trước khi trả về
                return [trai + 1, phai + 1]
                
            elif tong < target:
                # Nếu tổng đang nhỏ hơn mục tiêu, cần số lớn hơn -> Trái bước lên
                trai += 1
                
            else:
                # Nếu tổng đang lớn hơn mục tiêu, cần số nhỏ hơn -> Phải lùi lại
                phai -= 1