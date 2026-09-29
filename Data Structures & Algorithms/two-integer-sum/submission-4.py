class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if i == j:
        #             break
        #         if nums[i] + nums[j] == target:
        #             if j<i:
        #                 return [j,i]
        #             return [i,j]
        #             # return sorted([i,j])
        hashthing = {}
        for i in range(len(nums)):
            if target - nums[i] in hashthing:
                return[hashthing.get(target-nums[i]), i]
            else:
                hashthing[nums[i]] = i
            