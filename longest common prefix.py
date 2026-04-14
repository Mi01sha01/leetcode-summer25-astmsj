class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lon_com_pref = ""

        for i in zip(*strs):
            if len(set(i)) == 1:
                lon_com_pref += i[0]
            else:
                return lon_com_pref

        return lon_com_pref
