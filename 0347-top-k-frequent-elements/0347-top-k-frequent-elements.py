class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Bước 1: Đếm số lần xuất hiện (Bảng thống kê)
        kho_dem = {}
        for so in nums:
            kho_dem[so] = kho_dem.get(so, 0) + 1
            
        # Bước 2: Biến Dictionary thành một danh sách các cặp (số, tần suất xuất hiện)
        # Ví dụ: [(1, 3 lần), (2, 2 lần ), (3, 1 lần)]
        danh_sach_tan_suat = kho_dem.items()
        
        # Bước 3: Sắp xếp danh sách dựa trên tần suất (giảm dần)
        # key=lambda x: x[1] có nghĩa là: "Hãy nhìn vào con số thứ 2 trong cặp để xếp"
        danh_sach_tan_suat.sort(key=lambda x: x[1], reverse=True)
        
        # Bước 4: Lấy k phần tử đầu tiên và chỉ lấy cái tên số (phần tử thứ 0)
        ket_qua = []
        for i in range(k):
            ket_qua.append(danh_sach_tan_suat[i][0])
            
        return ket_qua