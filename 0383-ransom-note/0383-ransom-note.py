class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        kiem_tra = {}

        for chu_cai in magazine:
            kiem_tra[chu_cai] = kiem_tra.get(chu_cai, 0) + 1
        
        for chu_cai in ransomNote:
            if chu_cai not in kiem_tra or kiem_tra[chu_cai] == 0:
                return False

            kiem_tra[chu_cai] -= 1

        return True 