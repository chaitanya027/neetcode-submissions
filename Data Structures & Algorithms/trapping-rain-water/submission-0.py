class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        i,j = 0,len(height)-1
        left_max = height[i]
        right_max = height[j]

        max_water = 0
        while i<j:
            if left_max < right_max:
                i = i+1
                left_max = max(left_max, height[i])
                max_water += (left_max - height[i])
            else:
                j = j-1
                right_max = max(right_max, height[j])
                max_water += (right_max - height[j])
        return max_water
