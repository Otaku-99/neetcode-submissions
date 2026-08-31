class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi=0
        d=[]
        for i in range(len(s)):
            if s[i] in d:
                index = d.index(s[i])
                d = d[index + 1:]
            d.append(s[i])
            maxi = max(maxi,len(d))
        return maxi