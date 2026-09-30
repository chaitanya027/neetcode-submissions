class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        bag = {}
        for i, num in enumerate(nums):
            search = target - num
            if search in bag:
                return [bag[search],i]
            bag[num] = i