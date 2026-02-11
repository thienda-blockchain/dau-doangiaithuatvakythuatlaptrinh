class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        kho_nhom = {}

        for tu in strs:

            chu_cai_da_xep = sorted(tu)

            ten_nhom = "".join(chu_cai_da_xep)

            if ten_nhom in kho_nhom:

                kho_nhom[ten_nhom].append(tu)

            else:
                kho_nhom[ten_nhom] = [tu]

        ket_qua = []
        for nhom in kho_nhom:
            ket_qua.append(kho_nhom[nhom])

        return ket_qua
        