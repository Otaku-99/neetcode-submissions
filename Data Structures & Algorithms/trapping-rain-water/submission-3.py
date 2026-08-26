class Solution:
    def trap(self, height: List[int]) -> int:
        
        i, j = 0, len(height) - 1
        left_max, right_max = height[i], height[j]
        out = 0

        while i < j:
            if left_max <= right_max:
                i += 1
                left_max = max(left_max, height[i])
                out += left_max - height[i]
            else:
                j -= 1
                right_max = max(right_max, height[j])
                out += right_max - height[j]

        return out

        

        