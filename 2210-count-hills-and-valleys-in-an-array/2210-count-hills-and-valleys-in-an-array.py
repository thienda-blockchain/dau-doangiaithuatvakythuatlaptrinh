class Solution(object):
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # BƯỚC 1: RÚT GỌN MẢNG (Loại bỏ các số trùng nhau đứng cạnh nhau)
        # Bắt đầu mảng rút gọn với phần tử đầu tiên của nums
        rut_gon = [nums[0]] 
        
        # Duyệt từ phần tử thứ 2 đến cuối
        for i in range(1, len(nums)):
            # Nếu số hiện tại khác số ngay trước nó, ta mới đưa vào mảng rút gọn
            if nums[i] != nums[i-1]:
                rut_gon.append(nums[i])
                
        # BƯỚC 2: ĐẾM ĐỒI VÀ THUNG LŨNG TRÊN MẢNG ĐÃ RÚT GỌN
        count = 0
        
        # Duyệt qua mảng rút gọn (bỏ qua vị trí đầu và vị trí cuối vì chúng không thể là đỉnh)
        for i in range(1, len(rut_gon) - 1):
            
            # Kiểm tra Đồi (Hill): Lớn hơn cả hàng xóm trái và phải
            if rut_gon[i] > rut_gon[i-1] and rut_gon[i] > rut_gon[i+1]:
                count += 1
                
            # Kiểm tra Thung lũng (Valley): Nhỏ hơn cả hàng xóm trái và phải
            elif rut_gon[i] < rut_gon[i-1] and rut_gon[i] < rut_gon[i+1]:
                count += 1
                
        return count