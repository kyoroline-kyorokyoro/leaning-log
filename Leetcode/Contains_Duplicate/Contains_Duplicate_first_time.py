class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table={}
        for i in range(len(nums)):
            if nums[i]in table:return True
            table[nums[i]]=i
        return False
    
#最初にやったやり方。Two sumと同じハッシュテーブルの考えを
# 使ったけど、tableは別に辞書にしなくてよかったな。