# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        # CHỐT CHẶN: Nếu không còn phần tử nào để dựng cây thì trả về Rỗng (None)
        if not preorder or not inorder:
            return None
        
        # MANH MỐI 1 TỪ PREORDER: Tìm Rễ
        # Theo luật Preorder (Giữa-Trái-Phải), phần tử đầu tiên LUÔN LUÔN là Rễ của cây hiện tại.
        gia_tri_re = preorder[0]
        root = TreeNode(gia_tri_re) # Đắp đất nặn cái Rễ trước
        
        # MANH MỐI 2 TỪ INORDER: Tìm ranh giới Trái - Phải
        # Tìm vị trí của Rễ vừa nặn trong mảng Inorder.
        # Theo luật Inorder (Trái-Giữa-Phải), Rễ sẽ đứng giữa, chia mảng làm 2 phe: Trái và Phải.
        vi_tri_re_trong_inorder = inorder.index(gia_tri_re)
        
        # ĐỆ QUY XÂY DỰNG NHÁNH TRÁI VÀ NHÁNH PHẢI
        
        # 1. Xây nhánh Trái:
        # - Mảng Inorder của nhánh trái: Lấy từ đầu đến sát vị trí Rễ
        # - Mảng Preorder của nhánh trái: Bỏ qua phần tử đầu (là Rễ), lấy số lượng phần tử ĐÚNG BẰNG số phần tử của Inorder nhánh trái.
        root.left = self.buildTree(
            preorder[1 : vi_tri_re_trong_inorder + 1], 
            inorder[:vi_tri_re_trong_inorder]
        )
        
        # 2. Xây nhánh Phải:
        # - Mảng Inorder của nhánh phải: Lấy từ sau Rễ đến hết mảng
        # - Mảng Preorder của nhánh phải: Lấy phần còn lại của mảng Preorder
        root.right = self.buildTree(
            preorder[vi_tri_re_trong_inorder + 1 :], 
            inorder[vi_tri_re_trong_inorder + 1 :]
        )
        
        # Cuối cùng, trả về cái cây đã được lắp ráp hoàn chỉnh!
        return root