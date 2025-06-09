class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_low_nospace=''.join([c.lower() for c in s if c.isalnum()])
        s_revers=s_low_nospace[::-1]
        if s_low_nospace==s_revers:return True
        return False
    
# めっちゃ調べながらやった。
# join() はリストの要素をくっつけて、1つの文字列にする関数
# そして '' は 空文字だから：リストの要素を間に何も挟まずつなげる。

# スライス構文も復習
# s[start:stop:step]
# start	開始位置（含む）
# stop	終了位置（含まない）
# step	進み方（間隔、正なら前へ、負なら後ろへ）

# isalnum()	英字 (a-z, A-Z) か 数字 (0-9) なら True
# isalpha()	英字だけなら True
# isdigit()	数字だけなら True