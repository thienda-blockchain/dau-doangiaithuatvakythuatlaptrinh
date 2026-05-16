# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        # Hàm đệ quy mang theo "Giới hạn dưới" (low) và "Giới hạn trên" (high)
        def kiem_tra(node, gioi_han_duoi, gioi_han_tren):
            # CHỐT CHẶN: Đi đến tận cùng (hư không) mà không vi phạm luật -> Hợp lệ
            if not node:
                return True
            
            # KIỂM TRA LUẬT: Số hiện tại CÓ NẰM TRONG khoảng cho phép không?
            # Lưu ý: Phải dùng dấu <= và >= vì đề bài yêu cầu "nhỏ hơn/lớn hơn hẳn" (strictly)
            if node.val <= gioi_han_duoi or node.val >= gioi_han_tren:
                return False
            
            # ĐỆ QUY CHO 2 NHÁNH:
            # 1. Đi sang TRÁI: Tất cả các số bên trái phải NHỎ HƠN node hiện tại.
            #    -> Cập nhật "Giới hạn trên" = node.val
            nhanh_trai_hop_le = kiem_tra(node.left, gioi_han_duoi, node.val)
            
            # 2. Đi sang PHẢI: Tất cả các số bên phải phải LỚN HƠN node hiện tại.
            #    -> Cập nhật "Giới hạn dưới" = node.val
            nhanh_phai_hop_le = kiem_tra(node.right, node.val, gioi_han_tren)
            
            # Cả hai nhánh đều phải hợp lệ thì toàn bộ cây mới hợp lệ
            return nhanh_trai_hop_le and nhanh_phai_hop_le
        
        # Bắt đầu kiểm tra từ Rễ (Cụ Tổ). 
        # Rễ thì không bị giới hạn nên low là -Vô cùng, high là +Vô cùng
        return kiem_tra(root, float('-inf'), float('inf'))