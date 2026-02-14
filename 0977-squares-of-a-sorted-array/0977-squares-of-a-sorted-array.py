class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len (nums)
        answer = [0] * size 

        start = 0 
        end = size - 1
        index = size - 1

        while start <= end:
            left_value = nums[start]
            right_value = nums[end]

            if abs(left_value) >= abs(right_value):
                answer[index] = left_value * left_value
                start += 1
            else:
                answer[index] = right_value * right_value 
                end -= 1

            index -= 1

        return answer 


