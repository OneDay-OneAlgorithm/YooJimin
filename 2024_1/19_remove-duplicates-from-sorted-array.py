class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        remove_nums = list(set(nums))
        remove_nums.sort()
        
        for i, v in enumerate(remove_nums):
            nums[i] = v
            
        return len(remove_nums)