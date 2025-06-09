class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s==s[::-1]
    
# 正規表現（Regular Expression）というらしい。
# 文字列のパターンを記述するための特別な記法。
# 書き方が多すぎてまったく覚えられない。
# よく使うやつ	意味
# .	何か1文字
# *	直前のパターンを0回以上
# +	直前のパターンを1回以上
# []	中のどれか1文字
# [^]	中のどれでもない1文字
# \d	数字（0-9）
# \w	英数字＋アンダースコア
# \s	空白文字
# ^	文字列の先頭
# $	文字列の末尾
# re.sub(pattern, replacement, string)
# 引数　　　	意味
# pattern	正規表現パターン
# replacement	置き換える文字列
# string	対象の文字列

# [] → この中に含まれる文字のどれか
# a-z → 小文字の a から z
# A-Z → 大文字の A から Z
# 0-9 → 数字 0 から 9
# ^ → 否定！
# → これら以外の文字を意味する。