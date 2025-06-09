class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(t) == sorted(s)
#これしか思いつかなかった。ソートして比較。
# runtime 16 ms memory 18.70 MB