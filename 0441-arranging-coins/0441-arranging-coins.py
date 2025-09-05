class Solution:
    def arrangeCoins(self, n: int) -> int:
        low = 0
        high = n
        while(low<=high):
            mid = (low + high) // 2
            coins = mid * (mid + 1) // 2
            if(coins<n):
                low = mid + 1
            elif(coins>n):
                high = mid - 1
            else:
                return mid
        return high