class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       table={}
       for i in range(len(nums)):
            need=target-nums[i]
            if need in table:
                return[i,table[need]]    
            table[nums[i]]=i
#早い。優れた方法。O(n)の速度
#tableのキーに元の配列の値を入れて、値にキーを入れるのがミソ
# runtime 0 ms memory 19.06 MB
#あまりにも速い。０ミリ秒なんてあるか？