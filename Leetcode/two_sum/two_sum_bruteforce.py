class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range (i+1,len(nums)):
                if target==(nums[i]+nums[j]):
                    return [i,j]
#ブルートフォース。非効率。O(n^2)の速度
# runtime 1781 ms memory 18.24 MB