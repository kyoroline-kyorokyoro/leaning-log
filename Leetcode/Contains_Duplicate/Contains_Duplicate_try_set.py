class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table=set()
        for i in range(len(nums)):
            if nums[i]in table:return True
            table.add(nums[i])
        return False
        
#setというのがあるらしい。
# 重複と順序がない数のコレクションだそう。