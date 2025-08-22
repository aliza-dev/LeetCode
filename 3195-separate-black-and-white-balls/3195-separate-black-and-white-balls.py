class Solution(object):
    def minimumSteps(self, s):
        black_ball_count = 0
        total_swaps = 0
        for i in range (len(s)):
            if s[i] == "1":
                black_ball_count +=1
            else:
                total_swaps += black_ball_count
        return total_swaps

        