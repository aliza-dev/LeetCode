class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if s in (s+s)[1:-1]:
            return True
        else: 
            return False