class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 3:
            return 0
        
        # Bước 1: Tìm giá trị nhỏ nhất (min) và lớn nhất (max) của mảng
        # Một số x thỏa mãn đề bài khi và chỉ khi: min < x < max
        min_val = min(nums)
        max_val = max(nums)
        
        # Nếu min và max bằng nhau (tất cả các số trong mảng giống nhau)
        # thì kết quả chắc chắn là 0.
        if min_val == max_val:
            return 0
            
        count = 0
        
        # Bước 2: Duyệt qua mảng và đếm các số x nằm giữa min và max
        for x in nums:
            # Điều kiện "strictly" nghĩa là phải lớn hơn hẳn và nhỏ hơn hẳn
            if min_val < x < max_val:
                count += 1
                
        return count