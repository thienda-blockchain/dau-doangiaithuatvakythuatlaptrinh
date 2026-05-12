# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Lần này ta đoán từ 1 đến n (chứ không phải index từ 0)
        trai = 1
        phai = n
        
        # Bê nguyên xi vòng lặp bạn vừa bôi đen ở bài 704 sang đây!
        while trai <= phai:
            giua = (trai + phai) // 2
            
            # Hỏi anh MC xem số 'giua' mình đoán là đúng, cao hay thấp
            ket_qua_mc = guess(giua)
            
            if ket_qua_mc == 0:
                # Trúng phóc!
                return giua
                
            elif ket_qua_mc == -1:
                # MC bảo -1 nghĩa là: Số bạn đoán CAO HƠN kết quả
                # Nên ta phải bỏ nửa trên, tìm ở nửa dưới
                phai = giua - 1
                
            else: # ket_qua_mc == 1
                # MC bảo 1 nghĩa là: Số bạn đoán THẤP HƠN kết quả
                # Nên ta phải bỏ nửa dưới, tìm ở nửa trên
                trai = giua + 1
                
        return -1