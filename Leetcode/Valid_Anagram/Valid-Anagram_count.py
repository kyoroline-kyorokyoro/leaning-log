class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        for i in set(s):
            if s.count(i)!=t.count(i):return False
        return True
    
#ええ？めっちゃ早い。なんで。
# １．stringsの長さの比較
# ２．文字の出現回数を比較
# １で終わっちゃうケースが多かったのかな？
# runtime 0 ms memory 17.68 MB