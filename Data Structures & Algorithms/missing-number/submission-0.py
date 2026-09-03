class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = 0
        while True:
            if missing in nums:
                missing += 1
            else:
                return missing