class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # dedup = set(nums)
        # if list(dedup) != nums:
        #     return True
        # else:
        #     return False
        dedup = []
        for num in nums:
            if num not in dedup:
                dedup.append(num)
        if dedup != nums:
            return True
        else: 
            return False
