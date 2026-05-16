# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        # Hàm đệ quy phụ trợ để thu thập lá của một cây
        def thu_thap_la(node, danh_sach_la):
            # Chốt chặn: Đi vào ngõ cụt thì quay lại
            if not node:
                return
            
            # KIỂM TRA LÁ: Nốt không có con trái VÀ không có con phải
            if not node.left and not node.right:
                # Bứt lá bỏ vào giỏ (thêm vào mảng)
                danh_sach_la.append(node.val)
                return # Đã là lá thì không còn đường đi tiếp, quay lại luôn
            
            # ĐỆ QUY: Ưu tiên đi sang TRÁI trước để đảm bảo thứ tự từ trái sang phải
            thu_thap_la(node.left, danh_sach_la)
            
            # Sau khi hái hết lá bên trái, mới sang PHẢI để hái tiếp
            thu_thap_la(node.right, danh_sach_la)

        # Chuẩn bị 2 cái "giỏ" để đựng lá của 2 cây
        gio_la_cay_1 = []
        gio_la_cay_2 = []
        
        # Sai lính đi hái lá cho từng cây
        thu_thap_la(root1, gio_la_cay_1)
        thu_thap_la(root2, gio_la_cay_2)
        
        # So sánh xem 2 giỏ lá có giống hệt nhau (cả số lượng lẫn thứ tự) không
        return gio_la_cay_1 == gio_la_cay_2