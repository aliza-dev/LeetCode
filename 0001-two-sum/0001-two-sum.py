class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
           ## Two pointer approach
    #   left = 0
    #   right = len(nums)-1
    #   while left < right:
    #       total = nums[left] + nums[right]
    #        if (total == target):
    #           return [left,right]
    #        elif (total < taget):
    #            left+=1
    #        else:
    #            right-=1
    ## HashTable approach
        seen = {}
        for i, num in enumerate(nums):
            ans = target - num
            if ans in seen:
                return seen[ans],i
            else:
                seen[num] = i
