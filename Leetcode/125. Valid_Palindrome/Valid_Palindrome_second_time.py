class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_low_nospace=''.join([c.lower() for c in s if c.isalnum()])
        return s_low_nospace==s_low_nospace[::-1]
    
# ちょっとスッキリした。
# joinの使い方ね