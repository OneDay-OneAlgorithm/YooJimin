class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums_cnt = defaultdict(int)
        cnt = 0
        for i in range(len(nums)): 
            nums_cnt[nums[cnt]] += 1 
            if nums_cnt[nums[cnt]] == 3: 
                nums_cnt[nums[cnt]] -= 1
                del nums[cnt] 
                cnt -=1
            cnt += 1