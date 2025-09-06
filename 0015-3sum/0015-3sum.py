class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        Set = set()
        ans = []
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                Total = nums[i] + nums[j] + nums[k]
                if Total == 0:
                    Set.add((nums[i] , nums[j] , nums[k]))
                    k -= 1
                elif Total > 0:
                    k -= 1
                else:
                    j += 1
        for i in Set:
            ans.append(i)
        return ans