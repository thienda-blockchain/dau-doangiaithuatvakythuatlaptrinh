class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
         # Bước 1: Bắt buộc phải sắp xếp mảng để dùng chiến thuật 2 con trỏ
        nums.sort()
        
        # Khởi tạo "kỷ lục" ban đầu bằng tổng của 3 số đầu tiên trong mảng
        tong_gan_nhat = nums[0] + nums[1] + nums[2]
        
        # Bước 2: Chọn Đội trưởng (i) đi từ đầu đến áp chót
        for i in range(len(nums) - 2):
            
            # Hai người phụ việc đứng ở 2 đầu của phần mảng còn lại
            trai = i + 1
            phai = len(nums) - 1
            
            # Chừng nào 2 người phụ việc chưa chạm mặt nhau
            while trai < phai:
                tong_hien_tai = nums[i] + nums[trai] + nums[phai]
                
                # Nếu may mắn tìm được tổng bằng ĐÚNG target -> Khoảng cách = 0 (Hoàn hảo nhất)
                if tong_hien_tai == target:
                    return tong_hien_tai # Trả về ngay lập tức
                
                # Tính khoảng cách: Dùng hàm abs() để tìm giá trị tuyệt đối
                # Nếu khoảng cách của tổng hiện tại NHỎ HƠN khoảng cách của kỷ lục cũ
                if abs(target - tong_hien_tai) < abs(target - tong_gan_nhat):
                    tong_gan_nhat = tong_hien_tai # Cập nhật kỷ lục mới!
                    
                # CHIẾN THUẬT DỊCH CHUYỂN
                if tong_hien_tai < target:
                    # Đang bị thiếu điểm -> Người Trái bước sang phải để lấy số LỚN HƠN
                    trai += 1
                else:
                    # Đang bị dư điểm -> Người Phải bước sang trái để lấy số NHỎ HƠN
                    phai -= 1
                    
        return tong_gan_nhat