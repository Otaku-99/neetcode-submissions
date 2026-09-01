class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        left = 0
        max_freq = 0

        for right in range(len(s)):
            i = ord(s[right]) - 65
            count[i] += 1

            max_freq = max(max_freq, count[i])

            if right - left + 1 - max_freq > k:
                count[ord(s[left]) - 65] -= 1
                left += 1

        return len(s) - left