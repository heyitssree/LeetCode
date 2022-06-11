class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]]=i
        for i in range(len(nums)):
            expected = target - nums[i]
            if expected in hashmap and hashmap[expected] != i:
                return [i, hashmap[expected]]