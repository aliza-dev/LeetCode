class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        def helper(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        helper(0, len(nums)-1)
        helper(0, k-1)
        helper(k, len(nums)-1 )        