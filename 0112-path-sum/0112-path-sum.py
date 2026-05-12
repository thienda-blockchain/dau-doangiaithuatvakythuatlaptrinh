# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        # Nếu cây rỗng, đương nhiên không có đường đi nào
        if not root:
            return False
            
        # Trừ đi "nợ" ngay khi đặt chân đến nốt hiện tại
        so_no_con_lai = targetSum - root.val
        
        # ĐIỀU KIỆN DỪNG: Nếu đây là "chiếc lá" (không còn đường đi tiếp)
        if not root.left and not root.right:
            # Kiểm tra xem có trả hết nợ (số nợ còn lại == 0) hay không?
            return so_no_con_lai == 0
            
        # Nếu chưa phải lá, ta cử quân trinh sát đi tiếp xuống nhánh Trái và nhánh Phải
        # Chỉ cần MỘT trong hai nhánh tìm được kho báu (trả về True), ta sẽ thắng!
        di_nhanh_trai = self.hasPathSum(root.left, so_no_con_lai)
        di_nhanh_phai = self.hasPathSum(root.right, so_no_con_lai)
        
        return di_nhanh_trai or di_nhanh_phai