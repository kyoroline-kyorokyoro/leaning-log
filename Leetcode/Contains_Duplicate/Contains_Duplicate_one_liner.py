class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
    
#ワンライナー！！(というらしい？)これはかっこいい。
# set()が重複を消してくれるおかげで、
# 要素数が減るから、元のnumsとlen()を一発比較するだけでよい。
# 早いし読みやすい。