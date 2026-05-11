class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        dem_so = {} 
        
        ket_qua = -1
        so_lan_max = 0
        
        # Duyệt mảng từ đầu đến phần tử áp chót
        # (Dừng ở áp chót vì ta luôn cần nhìn vào số liền sau nó là nums[i+1])
        for i in range(len(nums) - 1):
            
            # Nếu tìm thấy key
            if nums[i] == key:
                target = nums[i + 1] # Lấy số đứng ngay sau nó
                
                # Cập nhật số lần xuất hiện vào sổ tay
                # Hàm .get(target, 0) nghĩa là: nếu chưa có trong sổ thì mặc định là 0
                dem_so[target] = dem_so.get(target, 0) + 1
                
                # Nếu số lần xuất hiện của số này lớn hơn kỷ lục hiện tại
                # thì cập nhật lại kỷ lục và ghi nhận nó làm kết quả
                if dem_so[target] > so_lan_max:
                    so_lan_max = dem_so[target]
                    ket_qua = target
                    
        return ket_qua