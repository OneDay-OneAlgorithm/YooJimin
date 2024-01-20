class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
#   ----------- SOL 1 --------------
#         half = len(nums) // 2
        
#         counter = Counter(nums)
        
#         for n, count in counter.items():
#             if count > half:
#                 return n

#   ----------- SOL 2 --------------
        return sorted(nums)[len(nums) // 2]
