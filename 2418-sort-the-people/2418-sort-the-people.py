class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        #Dùng Dic để gán tên và chiều cao song hành
        tu_tra_cuu = {}
        for i in range(len(names)):
            tu_tra_cuu[heights[i]] = names[i]

        heights.sort(reverse=True) #Sắp xếp số thứ tự từ lớn đến bé 

        ket_qua = []
        for h in heights:
            ten = tu_tra_cuu[h]
            ket_qua.append(ten)

        return ket_qua

