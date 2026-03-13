class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        nguyen_am = "aeiouAEIOU"
        cac_tu = sentence.split()
        
        ket_qua_list = []
        thu_tu = 1
        
        for tu in cac_tu:
            chu_dau = tu[0]
            tu_moi = ""
        
            if chu_dau in nguyen_am:
                tu_moi = tu + "ma"
            else:
                chu_con_lai = ""
                for i in range(1, len(tu)):
                    chu_con_lai += tu[i]
                
                tu_moi = chu_con_lai + chu_dau + "ma"
            
            for k in range(thu_tu):
                tu_moi += "a"
            
            ket_qua_list.append(tu_moi)
            thu_tu += 1
        return " ".join(ket_qua_list)