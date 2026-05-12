class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        trai = 0
        phai = len(nums) - 1
        
        while trai <= phai:
            giua = (trai + phai) // 2
            
            # Nếu may mắn trúng luôn ngay từ đầu
            if nums[giua] == target:
                return giua
                
            # Nếu số bên trái <= số ở giữa, nghĩa là từ 'trai' đến 'giua' là một đường tăng liên tục
            if nums[trai] <= nums[giua]:
                
                # Khi đã biết nửa trái là bình thường, ta kiểm tra xem target có lọt vào khoảng này không
                # Nghĩa là target phải lớn hơn hoặc bằng số nhỏ nhất (nums[trai]) 
                # và nhỏ hơn số lớn nhất (nums[giua])
                if nums[trai] <= target < nums[giua]:
                    # Nếu có, target chắc chắn nằm ở nửa trái
                    phai = giua - 1
                else:
                    # Nếu không, target bắt buộc phải nằm lẩn khuất ở nửa phải
                    trai = giua + 1
                    
            else:
                # Nửa phải là đường dốc tăng liên tục từ 'giua' đến 'phai'
                # Ta kiểm tra xem target có lọt vào khoảng an toàn này không
                if nums[giua] < target <= nums[phai]:
                    # Nếu có, thu hẹp về nửa phải
                    trai = giua + 1
                else:
                    # Nếu không, thu hẹp về nửa trái
                    phai = giua - 1
                    
        return -1