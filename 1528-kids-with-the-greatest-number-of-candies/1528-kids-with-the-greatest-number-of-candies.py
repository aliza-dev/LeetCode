class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        result = []
        for candy in candies:
            result.append(candy + extraCandies >= maximum)
        return result