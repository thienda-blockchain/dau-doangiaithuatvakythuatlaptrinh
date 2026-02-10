class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        tu_mau = strs[0]

        for i in range (len(tu_mau)):
            chu_cai_hien_tai = tu_mau[i]

            for j in range(1, len(strs)):
                tu_khac = strs[j]

                if i >= len(tu_khac) or tu_khac[i] != chu_cai_hien_tai:
                    return tu_mau[:i]
        
        return tu_mau


