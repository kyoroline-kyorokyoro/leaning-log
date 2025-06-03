class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        if len(set(s))!=len(set(t)):return False
        for i in set(s):
            if s.count(i)!=t.count(i):return False
        return True
    
# setを使ってみたかった。
# 普通にcountするより若干遅い。
# runtime 3 ms memory 18.04 MB