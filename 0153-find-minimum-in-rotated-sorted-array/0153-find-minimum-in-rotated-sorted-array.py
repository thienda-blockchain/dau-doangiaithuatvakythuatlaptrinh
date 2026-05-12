class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
         # Bước 1: Khởi tạo hai con trỏ trái và phải như mọi khi
        trai = 0
        phai = len(nums) - 1
        
        # Bước 2: Vòng lặp thu hẹp phạm vi
        # CHÚ Ý: Ở đây ta dùng < chứ không phải <=
        # Lý do: Ta đang tìm vị trí của một phần tử có thật, không phải tìm target.
        # Khi trai == phai, tức là ta đã dồn ép nó đến mức chỉ còn 1 phần tử duy nhất
        # Phần tử đó CHẮC CHẮN là số nhỏ nhất ta cần tìm.
        while trai < phai:
            giua = (trai + phai) // 2
            
            # Mấu chốt: So sánh phần tử ở giữa với phần tử ở cuối cùng (phai)
            # Tại sao? Vì phần tử cuối cùng sẽ cho ta biết nửa nào đang bị "gãy" (chứa đoạn xoay)
            
            # Trường hợp 1: Nếu số ở giữa lớn hơn số ở cuối
            # Ví dụ: [3, 4, 5, 1, 2], giua là 5, phai là 2. (5 > 2)
            # Điều này chứng tỏ đoạn bị "gãy" (chứa số nhỏ nhất) NẰM Ở NỬA PHẢI
            if nums[giua] > nums[phai]:
                # Ta thu hẹp vùng tìm kiếm sang nửa phải
                # (Lưu ý: giua chắc chắn không phải số nhỏ nhất vì nó > phai, nên ta bỏ qua nó luôn)
                trai = giua + 1
                
            # Trường hợp 2: Nếu số ở giữa nhỏ hơn hoặc bằng số ở cuối
            # Ví dụ: [5, 1, 2, 3, 4], giua là 2, phai là 4. (2 < 4)
            # Điều này chứng tỏ từ 'giua' đến 'phai' là một đường dốc tăng dần liên tục, không bị gãy.
            # Vậy số nhỏ nhất NẰM Ở NỬA TRÁI (hoặc chính là 'giua' luôn)
            else:
                # Ta thu hẹp vùng tìm kiếm sang nửa trái
                # (Lưu ý quan trọng: KHÔNG dùng phai = giua - 1, 
                # vì bản thân 'giua' có thể ĐANG CHÍNH LÀ SỐ NHỎ NHẤT)
                phai = giua
                
        # Khi vòng lặp kết thúc (trai == phai), ta trả về phần tử tại vị trí đó
        return nums[trai]